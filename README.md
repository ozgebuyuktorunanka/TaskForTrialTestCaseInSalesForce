# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Scenario Manager
>This Python script is designed to run and manage automation Scenarios for the Salesforce application. Below, you will find information on how to use this script and the main components it contains.

###  Important Notes:
>  You should carefully read "installation.md"  file before running the code.

## How to Run the Scenarios
1- Run the scneario manager
```python
- python ScenarioManager.pys
```
2- Enter the scenario number (1-5). Log in as required, and the scenario will be initiated.

## Requirements
Python 3.x is required to run this script.
Since the Selenium Python library is used, you may need to install Selenium. You can install it using the following command:
```python
- pip install selenium
```
## Scenario List
- TestScenario1, TestScenario2, TestScenario3, TestScenario4, and TestScenario5 classes represent each scenario.
- The corresponding scenario will be executed based on the scenario number.

## Salesforce Login
- Prior to running the script, you need to log in to your Salesforce account.
- The username and password should be defined in the login function.

```python
username = "ozgebuyuktorun@outlook.com"
password = "Ozge951357*"
```
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# TestScenario-1 : 
> This example scenario demonstrates how to create a new field in Salesforce with specific properties.
- 1.1	- Login to your Salesforce organization with your username and password.
- 1.2	- Go to the Setup > Object Manager > Account > Fields and Relationships.
- 1.3	- Create a new field with type:Text, label:Account Region, Length:255.

## Steps
- 1- Navigate to Setup > Object Manager > Account > Fields and Relationships in Salesforce.
- 2- Click the "New" button to create a new field.
- 3 - Set the field properties 
    - 3.1 -Type: Text
    - 3.2 -Label: Account Region
    - 3.3 - Length: 255
    -3.4 -  Save the new field.

# Python Code
>>  Some libraries . 
```python
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
```
### Notes:
- When specifying the scenario number, make sure to enter a number between 1 and 5. Entering a number outside this range will result in an invalid scenario.
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Test Scenario 2 - Automating Account and Contact Creation
  Automates the process of creating a new Account and a Contact in Salesforce. The script uses Selenium for web automation and follows a specific set of steps to achieve this. Below, you'll find details on how to use the script and a breakdown of the scenario.

## How to Run the Scenarios

1. Run the Scenario Manager script:

    ```python
    python ScenarioManager.py
    ```

2. Enter scenario number 2 when prompted, and the script will handle the rest.

## Scenario Steps

### 2.1 - Go to the Accounts tab

The script navigates to the Salesforce Accounts tab using the Lightning interface.

### 2.2 - Create a new Account

A new Account is created with the name "CyanGate" and the region set to "EMEA."

### 2.3 - Confirm the Account is saved

After creating the Account, the script confirms that the record is successfully saved.

### 2.4 - Go to the Contacts tab

The script switches to the Contacts tab.

### 2.5 - Create a new Contact

A new Contact is created with the following details:
- First Name: Brad
- Last Name: Scott
- Account Name: CyanGate
- Language: English

### 2.6 - Confirm the Contact is saved

After creating the Contact, the script confirms that the record is successfully saved.

### 2.7 - Verify Account Name on Contact

The script checks whether the Account Name is set as "CyanGate" on the Contact record.

### 2.8 - Go back to the Accounts tab

The script returns to the Accounts tab.

### 2.9 - Navigate to the CyanGate record

The script searches for and proceeds to the "CyanGate" Account record.

### 2.10 - Confirm Brad Scott is visible as a contact

The script hovers over the Contact record and verifies that "Brad Scott" is visible in the Contacts section under the Related tab.
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Test Scenario 3 - Managing Account Ownership
> Automates the process of managing account ownership in Salesforce. It performs actions to change the account owner and verifies the changes. Below, you'll find a detailed breakdown of the scenario.

## How to Run the Scenarios

1. Run the Scenario Manager script:

    ```python
    python ScenarioManager.py
    ```

2. Enter scenario number 3 when prompted, and the script will handle the rest.

## Scenario Steps

### 3.1 - Go to the Account Details section
The script navigates to the Salesforce Accounts tab and selects an account to view its details.

### 3.2 - Verify Account Owner
The script verifies that the Account Owner field shows you as the logged-in user. It compares your profile name with the name in the details section.

### 3.3 - Click on the Change Owner button

The script clicks on the "Change Owner" button to initiate the ownership change process.

### 3.4 - Search for "Integration User"

A search for the user named "Integration User" is performed in the Change Owner dialog.

### 3.5 - Select "Integration User" as the new owner

The script selects "Integration User" as the new owner and confirms the change.

### 3.6 - Verify Account Owner Change

The script verifies that the Account owner is now "Integration User" and compares it with the initial owner.
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Test Scenario 4 - Managing File Upload and Download
> Automates the process of uploading files to the "Notes & Attachments" section and downloading them from a Salesforce account. It also verifies the completeness of file uploads and their presence in the local folder.

## How to Run the Scenarios

1. Run the Scenario Manager script:

    ```python
    python ScenarioManager.py
    ```

2. Enter scenario number 4 when prompted, and the script will handle the rest.

## Scenario Steps

### 4.1 - Upload Files

The script navigates to a specific user's Salesforce account page and goes to the "Files" section. It then clicks on "Upload Files."

### 4.2 - Verify Uploads

-  The script uploads a file and verifies that the upload is complete.
-  It checks that the uploaded file's name matches the expected document name.

### 4.3 - Download Files

The script then recursively performs the following steps for all uploaded files:

#### 4.3.1 - Click on a File

The script clicks on one of the uploaded files.

#### 4.3.2 - Verify File Download

It verifies that the file is successfully downloaded and visible in the provided folder path.

#### 4.3.3 - Delete Local File

The script deletes the downloaded file from the local folder.
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Test Scenario 5 - Managing Email Composition and Sending
> Automates the process of composing and sending an email through a Salesforce account. It also verifies the successful sending of the email.

## How to Run the Scenarios

1. Run the Scenario Manager script:

    ```python
    python ScenarioManager.py
    ```

2. Enter scenario number 5 when prompted, and the script will handle the rest.

## Scenario Steps

### 5.1 - Navigate to Contacts

The script navigates to the "Contacts" tab in Salesforce.

### 5.2 - Select a Contact

It selects a contact from the contacts list, specifically "Brad Scott."

### 5.3 - Compose an Email

The script clicks on the "Email" section in the Activity tab, opening the email composition window.

### 5.4 - Verify Sender Information

It verifies that the "From" section is not blank and displays the sender's email address.

### 5.5 - Add Recipient Email Address

A valid recipient email address, "ozgeesert@gmail.com," is added to the "To" section.

### 5.6 - Enter Email Subject

The email subject is set as "Test Email."

### 5.7 - Compose Email Body

In the email's body section, the script types "Test Body."

### 5.8 - Attach a File

It clicks on the "Attach file" button under the email body area.

### 5.9 - Select a File

The script selects one of the previously uploaded files and clicks "Add."

### 5.10 - Verify Attachment

It verifies that the file is attached to the email.

### 5.11 - Send the Email

The email is sent by clicking on the "Send" button.

### 5.12 - Verify Email Sent

The script verifies that the email is successfully sent and displays a success message.



