from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os, time

from LogFile import LogFile

class TestScenario4:
    def __init__(self, driver):
        self.driver = driver
    def initialize(self):
        self.driver.maximize_window()
        self.run_test()
        log = LogFile()
        self.log.log("Test Scenario 4: Starting the scenario...")

    def run_test(self):
    # 4.1	On the “Test Account” page, upload 4 files to the Notes&Attachments section under the Related tab.
        wait=WebDriverWait(self.driver,10)
        wait.until(EC.url_to_be("https://loteccompany-dev-ed.develop.lightning.force.com/lightning/setup/SetupOneHome/home"))
        print("The page loaded successfully!")  #for control

        icon_waffle = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".slds-icon-waffle")))
        icon_waffle.click()
        self.driver.implicitly_wait(10)
        search_area = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='View All Applications']")
        search_area.click()
        accounts_element= self.driver.find_element(By.XPATH,"//*[@id='input-120']")
        # accounts_element= self.driver.find_element(By.LINK_TEXT,"Accounts")
        accounts_element.click()
        accounts_element.send_keys("People")
        self.driver.implicitly_wait(10) 
       
        people_button = self.driver.find_element(By.CSS_SELECTOR,"p[class='slds-truncate'] mark")
        people_button.click()
        #account user's page openning.
        user_name ='Özge Büyüktorun'
        user_find_element = self.driver.find_element(By.LINK_TEXT,f"{user_name}")
        # user_find_element = self.driver.find_element(By.XPATH,"//a[contains(text(),f'{user_name}')]")        
        user_find_element.click()
        self.driver.implicitly_wait(10)
        
        # The mouse move to the files upload section 
        files_upload_area = self.driver.find_element(By.XPATH,"//article[@aria-label='Files']//div[@class='slds-grid slds-page-header forceRelatedListCardHeader']")
        action = ActionChains(self.driver)
        action.move_to_element(files_upload_area).perform() 

        view_all_button = self.driver.find_element(By.XPATH,"//div[@class='slds-card__footer']")
        view_all_button.click()
    # 4.2	Verify that the uploads are complete.
        upload_files_button = self.driver.find_element(By.XPATH,"//a[@title='Upload Files']")
        upload_files_button.click()
        expected_document_name = "Özgeçmiş1"
        # user select a file from desktop and enter Open button and then the code will continue.
        done_button = wait.until(EC.visibility_of_element_located(By.XPATH,"//button[contains(@class, 'slds-button--neutral') and contains(@class, 'ok') and contains(@class, 'desktop')]"))
        done_button.click()
        self.driver.implicitly_wait(5)
        visible_document_name= self.driver.find_element()
        document_name = visible_document_name.text

        assert expected_document_name == document_name, "The documents does not match"; f"The documents match real doc: {expected_document_name}, visible doc: {visible_document_name}"
        
        table = self.driver.find_element(By.XPATH, "//tbody[@data-aura-rendered-by='2937:0']")
        search_doc_name = expected_document_name
        #all row
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            # Her satırın altındaki "title" sütununu bulun
            title_column = row.find_element(By.XPATH, ".//th[@scope='row']//span[@title]")
            doc_names = title_column.get_attribute("title")  #title's text getting

            if search_doc_name in doc_names:
                print(f"{search_doc_name}  file is founded.")

    # 4.3	RECURSIVELY complete the following steps FOR ALL FILES:
    # 4.3.1	Click on one of the files.
        file_link = self.driver.find_elemen(By.XPATH,"//span[@class='itemTitle desktop outputTextOverride uiOutputText' and @title='Özgeçmiş1']")
        file_link.click()
    # 4.3.3	Verify that the file is downloaded and visible in the provided folder path.
        download_button = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[5]/div[2]/div/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/div/div/button/span")
        download_button.click()
        users = "ozges"
        filename= "Downloads"
        download_file_path = f"C:\\Users\\{users}\\{filename}"
        time.sleep(5) 
        file_path = os.path.join(download_file_path, f'{search_doc_name}.pdf')

    # 4.3.4	Delete the file from local.
        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
                print("The file has been successfully deleted.")
            except Exception as e:
                print(f"An error occurred while deleting the file: {str(e)}")
        else:
            print("The file does not exist in the specified folder.")
        

        self.log.log("Test Scenario 4: Scenario completed.")
        self.driver.quit()
