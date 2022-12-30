# Data Representation Project 2022

## Description

This repository was created to complete the project for Data Representation module.

Task: Write a program that demonstrates that you understand creating and consuming RESTful APIs.

I decided to create web app where students can register and enroll in modules. There is a functionality to perform CRUD operations on the data. 

## Explore

Repository Contents:
1. gitignore
2. README.md
3. LICENSE
4. app.py - flask server file
5. collegeDAO.py - deals with Database, connections and converting formats
6. initdb.sql - file which is used to create DB and add some data to it
7. requirements.txt
8. config_temp.py

Folders:
1. static:
    - style.css file
2. templates 
    - index.html, 
    - login.html, 
    - register.html

## How to implement this web application on your local machine:

### Installation
1. Python ( I have used Python 3.8.3). I would recommend anaconda installation Anaconda.
2. Install MySQL (MySQLWorkbench if on Mac).
3. Clone this repository (Click on the green button "Code". Select "Clone with HTTPS". Copy the URL.)
4. Select the folder on your local machine using terminal, type `git clone` and paste the link.
5. Create virtual environment
6. To install the necessary packages in the same folder/directory excecute the following: `pip install -r requirements.txt`
7. In MySQL create a database called "dataRep". Use the initdb.sql to create the tables & insert records for testing in a database called dataRep.
8. Create a file called config.py using config_temp.py as a template. Enter your own username & password here.

### Execution
1. In your terminal navigate to the the folder where you cloned this repository.
2. Activate virtual environment
3. `set FLASK_APP=app`
4. `flask run` In your browser navigate to http://127.0.0.1:5000/

## This web app is hosted online on pythonanywhere.com
http://angelinka.pythonanywhere.com/

### Side note: 
A few improvements could be made on this web app, mainly including better exception handling, cleaner code and better functionality. However as time was of the essence I hope it will suffice to demonstrate my overall understanding of Flask & RESTful API.

## Contact

[angelb511@gmail.com](mailto:angelb511@gmail.com)