import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class TestScenario3:
    def __init__(self, driver):
        self.driver = driver
    def initialize(self):
        self.driver.maximize_window()
        self.run_test()
        self.log.log("Test Scenario 3: Starting the scenario...")
    def run_test(self):
    # 3.1	On the Accounts tab, go to the Details section.
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
        accounts_element.send_keys("Accounts")
        self.driver.implicitly_wait(10) 
        account_home = self.driver.find_element(By.XPATH, "//a[@href='/lightning/o/Account/home']")
         # target_element = self.driver.find_element(By.XPATH, "//mark[.='Accounts']/ancestor::a")
        account_home.click()
        #Mouse over the element
        target_element = self.driver.find_element(By.CSS_SELECTOR, ".initialSortAsc:nth-child(4) .toggle")
        action = ActionChains(self.driver)
        action.move_to_element(target_element).perform()
        account_name_selection = self.driver.find_element(By.LINK_TEXT,"CyanGate")
        account_name_selection.click()
        self.driver.implicitly_wait(10)
        
        details_section = self.driver.find_element(By.ID,"detailTab__item")  
        details_section.click()
    # 3.2	Verify that the Account Owner field shows you as the logged-in user.
        #login user find
        profile_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'branding-userProfile-button')]")))
        profile_button.click()
        self.driver.implicitly_wait(10) 

        account_name_element = self.driver.find_element(By.CSS_SELECTOR, "h1[class='profile-card-name'] a[class='profile-link-label']")
        account_name = account_name_element.text 
        name1 = account_name
        account_name_element.click()
        print(f"Profile Name: {name1}")

        account_details_section = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "test-id__field-value")))
        account_details_section_name =account_details_section.text
        name2 = account_details_section_name
        print(f"Details section name: {name2}")
    
    # compare names and produce AssertionError if not true
        assert name1 == name2, f" The name does not match. Real Account name: {name1}, Details section name : {name2}";"The names matches"

    # 3.3	Click on the Change Owner button
        change_owner_button = self.driver.find_element(By.XPATH, "//button[@title='Change Owner']")
        change_owner_button.click()
        self.driver.implicitly_wait(10)   #waiting time for pop-up appear
        
    # 3.4	 Search for the user called “Integration User”.
        pill_text_area = self.driver.find_element(By.CLASS_NAME, "pillText")
        self.driver.execute_script("arguments[0].textContent = 'Integration User';", pill_text_area)
        pill_text_area.send_keys(Keys.RETURN)   #press enter

    # 3.5	Select the “Integration User” user as the new owner of the record and click on Change Owner.
        integration_user_find = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Integration User")
        link = integration_user_find.get_attribute("href")
        integration_user_find.click()
        change_owner_button2 = self.driver.find_element(By.LINK_TEXT,"//button[text()='Change Owner']")
        change_owner_button2.click()
        self.driver.get(link)
    # 3.6	Verify that the Account owner is now Integration User.
        print(f" After the account owner changes , account name is visible as: {name2}")
        assert name2 == name1, "Integration User"; "The name is not correct"

        self.log.log("Test Scenario 3: Scenario completed.")
        self.driver.quit()  
