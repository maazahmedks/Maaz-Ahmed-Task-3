Backend API Automation
----------------------
This is an example of backend API automation project, written using Python tytest.

Purpose
-------
This project was developed by me to demonstrate how to perform Backend API automation in which system communicate with the APIs.

Technology Stack
----------------
- Python
- Pytest
- Assertions

Prerequisites & Versions
------------------------
Python - Language & Virtual enviroment
Pycharm - IDE

Test Execution
---------------
Following command is used to run all tests marked as smoke.

pytest -m pet


Folders and Files details
---------------------------
Below are the details of files:
- petstore3.apiautotest.tests contains folder having test script.
- petstore3.apiautotest.src.configs.host_config.py contains file having environment URLs.
- petstore3.apiautotest.src.dao.pet_dao.py contains file use to execute database queries.
- petstore3.apiautotest.src.Helpers.PetHelpers.py contains file having functions that is used to execute APIs.
- petstore3.apiautotest.src.Utilities.CredentialsUtility.py contains API keys and database functions.
- petstore3.apiautotest.src.Utilities.DbUtility.py contains functions use to create database connection.
- petstore3.apiautotest.src.Utilities.GenericUtilities.py contains functions in the test script various times.
- petstore3.apiautotest.src.Utilities.requestUtilities.py contains functions for API methods.
