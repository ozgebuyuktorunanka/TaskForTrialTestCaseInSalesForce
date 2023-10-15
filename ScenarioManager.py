from selenium import webdriver
from LogFile import LogFile
from TestScenario1 import TestScenario1
from TestScenario2 import TestScenario2
from TestScenario3 import TestScenario3
from TestScenario4 import TestScenario4
from TestScenario5 import TestScenario5
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ScenarioManager:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.log = LogFile()
        self.initialize_driver()

    def login(self):      
        self.driver.get("https://login.salesforce.com")
        wait = WebDriverWait(self.driver, 10)
        # Enter data in the username and password fields
        username = "ozgebuyuktorun@outlook.com"
        password = "Ozge951357*"
        # Username and password areas 
        self.driver.implicitly_wait(20)  
        username_field = self.driver.find_element(By.ID, "username")
        username_field.send_keys(username)
        self.driver.implicitly_wait(10)  
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        # Login button click
        self.driver.find_element(By.ID,"Login").click() 

    def run_scenario(self, scenario_number):
        self.login()   #Scenario 1 - 1.1 item
        if scenario_number == 1:
            scenario = TestScenario1(self.driver)
            scenario.initialize() 
        elif scenario_number == 2:
            scenario = TestScenario2(self.driver)
            scenario.initialize()
        elif scenario_number == 3:
            scenario = TestScenario3(self.driver)
            scenario.initialize()
        elif scenario_number == 4:
            scenario = TestScenario4(self.driver)
            scenario.initialize()
        elif scenario_number == 5:
            scenario = TestScenario5(self.driver)
            scenario.initialize()
        else:
            print("Invalid scenario number.")

        if scenario_number in range(1, 6):
            self.log.log(f"Running Scenario {scenario_number}")
            scenario.initialize()
            self.log.log(f"Scenario {scenario_number} completed")

        self.driver.quit()


    def initialize_driver(self):
        #Case Number Selection Side
        scenario_num= int(input("Which scenario you want to run, write (1-5): "))
        if 1 <= scenario_num < 6:
           self.run_scenario(scenario_num)
        else:
            print("Invalid scenario number.")

if __name__ == "__main__":
    log = LogFile()
    # log.clear_log()
    manager = ScenarioManager()
    scenario_number = int(input("Which scenario you want to run, write (1-5): "))
    manager.run_scenario(scenario_number)
