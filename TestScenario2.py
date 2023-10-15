import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class TestScenario2:
    def __init__(self, driver):
        self.driver = driver

    def initialize(self):
        self.create_account()
        self.log.log("Test Scenario 2: Starting the scenario...")

    def create_account(self):
        #2.1 Go to the Accounts tab
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
        # 2.2 Create a new Account with Account Name:"Cyngate", Account Region : EMEA
        new_account_add_button = self.driver.find_element(By.LINK_TEXT, "New")
        new_account_add_button.click()
        self.driver.implicitly_wait(10)

         # New Account Adding Process
        account_name = self.driver.find_element(By.ID, "input-163")
        account_name.click()
        account_name.send_keys("CyanGate")

        #AccountRegion 
        self.driver.execute_script("window.scrollTo(0,0)")
        region_area=self.driver.find_element(By.ID, "input-232")
        actions = ActionChains(self.driver)
        actions.move_to_element(region_area).perform()
        # region_area.click()
        region_area.send_keys("EMEA") 
        self.driver.implicitly_wait(10)

        # 2.3  Confirm that the Account record is saved.
        self.driver.execute_script("window.scrollTo(0,0)")
        save_button = self. driver.find_element(By.NAME, "SaveEdit")
        save_button.click()
   
         #2.4 Go to the Contacts tab.
        time.sleep(10)
        contacts_buttton = self.driver.find_element(By.CSS_SELECTOR,"a[title='Contacts']")
        contacts_buttton.click()
        time.sleep(10)
        # 2.5 Create a new contact with the following information
        new_button =  self.driver.find_element(By.XPATH, "//div[@title='New']")
        new_button.click()
        self.driver.implicitly_wait(10)

            #----------------------------------------pop-up opened-------------------------------------------------------------------------------------
        # 2.5.1 First Name: Brad
        first_name = self.driver.find_element(By.XPATH,"//*[@id='input-743']")
        first_name.click()
        first_name.send_keys("Brad")

        # 2.5.2 Last Name: Scott
        last_name = self.driver.find_element(By.CSS_SELECTOR,"#input-745")
        last_name.click()
        last_name.send_keys("Scott")

        target_element = self.driver.find_element(By.CSS_SELECTOR, ".actionBody")
        action = ActionChains(self.driver) #create a action object
        action.move_to_element(target_element).click_and_hold().perform()
        action.move_by_offset(787.5, 474).perform()
  
            # 2.5.3 Account Name: CyanGate
        dropdown = self.driver.find_element(By.ID,"combobox-input-296")
        dropdown.find_element(By.XPATH, "//option[. = 'Cyangate']").click()

        # 2.5.4 Languages: English
        self.driver.execute_script("window.scrollTo(0, 0)")
        language_seletion = self.driver.find_element(By.ID, "input-275")
        language_seletion.click()
        language_seletion.send_keys("English")

        self.driver.find_element(By.CSS_SELECTOR,".fixedFooter").click()  #empty field clicking.

        # 2.5.5  Account Region: EMEA -> There is not any input area about region. For this reason, I can not choose 'EMEA' .

        # 2.6  Confirm that the Contact record is saved
        save_button2 = self.driver.find_element(   By.NAME,"SaveEdit")
        save_button2.click()
        #-----------------------------------------------------pop-up closed------------------------------------------------------------------------
        # 2.7 Verify that the Account Name is set as “CyanGate” on the Contact.
        column_name = "Account Name"
        xpath = f"//td[@role='gridcell' and contains(@class, 'forceInlineEditCell')]//a[contains(text(), '{column_name}')]/ancestor::td"
        account_name_elements = self.driver.find_elements(By.XPATH, xpath)

        # Check for the presence of a value containing the name CyanGate
        is_cyan_gate_present = False
        for element in account_name_elements:
            if "CyanGate" in element.text:
                is_cyan_gate_present = True
                break

        # Result
        if is_cyan_gate_present:
            print("It has a record with Account Name set as CyanGate.")
        else:
            print("It does not have a record with Account Name set as CyanGate.")

        # 2.8 Go to the Accounts tab.
        account_home.click()

        # 2.9 Proceed to the CyanGate record.
        search_list = self.driver.find_element(By.ID,"input-120")
        search_list.click()
        search_list.send_keys="CyanGate"
        self.driver.find_element(By.LINK_TEXT,"CyanGate").click()

        # 2.10 Under the Related tab, confirm that Brad Scott is visible as a contact in Contacts section.
        # Mouse over process
        brad_control = self.driver.find_element(By.CSS_SELECTOR, '.outputLookupLink-0038e00000Iv9gwAAB-137\3A 1552\;a')
        ActionChains(self.driver).move_to_element(brad_control).perform()

        # Set waiting time and catch pop-up window
        popup_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.outputLookupLink-0038e00000Iv9gwAAB-137\3A 1552\;a')))

        # Pop-Up window control
        if "Brad" in popup_element.text and "Scott" in popup_element.text:
            print("Brad Scott information was found in the pop-up window.")
        else:
            print("This information was not found in window.")

        self.log.log("Test Scenario 2: Scenario completed.")
        self.driver.quit()  