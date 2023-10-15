from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from LogFile import LogFile

class TestScenario1:
    def __init__(self, driver):
        self.driver = driver
        self.log=LogFile()

    def initialize(self):
        self.create_account_region_field()
        self.log.log("Test Scenario 1: Starting the scenario...")

    def create_account_region_field(self):
        # 1.2  Go to the Setup > Object Manager > Account > Fields and Relationships.
        print("The page loaded successfully!")
        wait=WebDriverWait(self.driver,10)
        # Setup Home Link Click
        self.driver.implicitly_wait(10)   #implicity wait for page loading.
        setup_click= self.driver.find_element(By.XPATH, "//a[normalize-space()='Setup Home']")
        setup_click.click()
        # Go to Object Manager
        objectmanager= self.driver.find_element(By.XPATH,'//a[@title="Object Manager"]')
        objectmanager.click()
        # Go to Account
        account=self.driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(1) th:nth-child(1) a:nth-child(1)")
        account.click()
        relations_button_xpath = '//a[@role="tab" and contains(@href, "/FieldsAndRelationships/view")]'
        wait.until(EC.element_to_be_clickable((By.XPATH, relations_button_xpath))).click()

        #1.3	Create a new field with type:Text, label:Account Region, Length:255.
        #new button add
        new_add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Custom Field']")))
        # self.driver.find_element(By.CSS_SELECTOR, ".slds-button--neutral:nth-child(1)").click()
        new_add_button.click()     
        self.driver.switch_to.frame(0)   #iframe in
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(12) label").click()
        self.driver.find_element(By.CSS_SELECTOR, ".pbBottomButtons > .btn").click()

        field_label = self.driver.find_element(By.ID, "MasterLabel")
        field_label.click()  
        field_label.send_keys("Account Region2323")
        
        length = self.driver.find_element(By.ID, "Length")
        length.click()
        length.send_keys("255")
        self.driver.find_element(By.ID, "Description").click() #free click area
        scroll_distance = 500
        self.driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
        self.driver.find_element(By.CSS_SELECTOR, ".pbTopButtons > input[name='goNext']").click()  #next button1 clickin
        self.driver.find_element(By.CSS_SELECTOR, ".pbTopButtons > input[name='goNext']").click()  #next button2 clickin
        self.driver.find_element(By.CSS_SELECTOR, ".pbTopButtons > input[name='save']").click()  #next button2 clickin

        self.driver.switch_to.default_content()  #iframe out
        self.log.log("Test Scenario 1: Scenario completed.")
        self.driver.quit()
