import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class TestScenario5:
    def __init__(self, driver):
        self.driver = driver

    def initialize(self):
        self.driver.maximize_window()
        self.run_test()
        self.log.log("Test Scenario 5: Starting the scenario...")
        

    def run_test(self):
    # 5.1	Go to the Contacts tab.
        wait=WebDriverWait(self.driver,10)
        wait.until(EC.url_to_be("https://loteccompany-dev-ed.develop.lightning.force.com/lightning/setup/SetupOneHome/home"))
        print("The page loaded successfully!")  #for control

        icon_waffle = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".slds-icon-waffle")))
        icon_waffle.click()
        self.driver.implicitly_wait(10)
        view_all_button = self.driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[2]/div[1]/div[2]/one-app-launcher-menu/div/lightning-button/button")
        self.driver.implicitly_wait(10)
        view_all_button.click()

        accounts_element= self.driver.find_element(By.XPATH,"//*[@id='input-120']")
        # accounts_element= self.driver.find_element(By.LINK_TEXT,"Accounts")
        accounts_element.click()
        accounts_element.send_keys("Contacts")
        self.driver.implicitly_wait(10) 
       
        contacts_button = self.driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[2]/div[2]/div/div[2]/one-app-launcher-modal/div/div[2]/lightning-accordion/div/slot/lightning-accordion-section[2]/div/section/div[2]/slot/ul/li/one-app-launcher-tab-item/a")
        contacts_button.click()
        time.sleep(10)
        search_in_contacts = self.driver.find_element(By.ID ,"input-120")
        search_in_contacts.click()
        search_in_contacts.send_keys("Brad Scott")

    # 5.2	5.2 Select Brad Scott from the contacts list.
        find_brad = self.driver.find_element(By.LINK_TEXT ,"Brad Scott")
        find_brad.click()

    # 5.3	On the Activity tab on the right, click on Email section.
        email_button = self.driver.find_element(By.XPATH,"//button[contains(@title,'Email')]")
        email_button.click()
        self.driver.implicitly_wait(10)

    # 5.4	Verify that the From section is not blank.
        from_section = self.driver.find_element(By.XPATH ,"//a[@role='button'][normalize-space()='Özge Büyüktorun <ozgebuyuktorun@outlook.com>']")
        from_section.click()
        email_from_text = from_section.text
        if email_from_text:
            print("This email from area is not blank. Include a email address.")
        else:
            print("The email from whom section is blank. please write a correct email address.")
            
    # 5.5	Type a valid email address to the To section.
        from_section.send_keys("ozgeesert@gmail.com")

    # 5.6	Enter subject as “Test Email”.
        subject = self.driver.find_element(By.XPATH,"//body[@class='desktop slds-wcag']/div[4]/div[@class='viewport']/section/div[@class='flexipagePage']/div[1]/div[5]//div[@role='dialog']//div[@class='forceChatterPublisherPresentationDesktop forceChatterPublisherQuickAction supportPublisherQuickSendEmail']//div[@class='cuf-content scrollable']/section//div[@class='MEDIUM sendEmailQuickActionBody supportSendEmailQuickAction']/div[1]/section/div/div/div/div/div/div[5]/div//input[@placeholder='Enter Subject...']")
        subject.click()
        subject.send_keys("Test Email")

    # 5.7	On the email’s body section, type “Test Body”.
        body = self.driver.find_element(By.CSS_SELECTOR, "body")
        body.send_keys("Test Body")

    # 5.8	Click on Attach file under Body area of the email.
        attached_file = self.driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/section/div[2]/div[1]/div[5]/div/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/div/ul/li[1]/div/button")
        attached_file.click()
    # 5.9	Select one of the files previously uploaded and click Add.
        #file selection checkbox
        self.driver.implicitly_wait(10)
        checkbox = self.driver.find_element(By.CSS_SELECTOR, ".slds-var-p-horizontal_medium:nth-child(1) .itemTitle")
        checkbox.click()
    #add buton and attached the file to the email.
        add_button = self.driver.find_element(By.CSS_SELECTOR,".attach")
        add_button.click()
        self.driver.implicitly_wait(10)
        
    # 5.10	Verify that the file is attached.
        try:
            control_area = wait.until(EC.visibility_of_element_located(By.XPATH, "//span[@title='Preview file' and contains(@class, 'uiOutputText')]"))
            control_area.click()
            print("There is a attachment file.")
        except NoSuchElementException:
            print("There is not a file in this e-mail.")

    # 5.11	Click on Send.
        send_button = self.driver.find_element(By.CSS_SELECTOR,".slds-button--brand")
        send_button.click()
        self.driver.implicitly_wait(10)  #for see alert dialog  box
     
    # 5.12	Verify that the email is sent with a success message.
        try:
            alert_dialog = self.driver.find_element(By.CSS_SELECTOR,"//body[@class='desktop slds-wcag']/div[6]//div[@role='alertdialog']")
            alert_dialog.click()
            control_message = alert_dialog.text
            expected_text ="Email was sent"
            assert control_message == expected_text, "Don't see success message.";"The successfull message is visible."
        except NoSuchElementException:
            print("The alert message is not visible.")

        self.log.log("Test Scenario 5: Scenario completed.")
        self.driver.quit()
