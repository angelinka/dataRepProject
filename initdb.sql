CREATE DATABASE IF NOT EXISTS dataRep;

USE dataRep;

CREATE TABLE IF NOT EXISTS modules(
   moduleCode VARCHAR(255) NOT NULL,
   moduleName VARCHAR(255) NOT NULL,
   location VARCHAR(255) DEFAULT NULL,
   credits INT NOT NULL,
   PRIMARY KEY (moduleCode)
   );


CREATE TABLE IF NOT EXISTS students(
   studentID INT NOT NULL AUTO_INCREMENT,
   email varchar(255) NOT NULL,
   password varchar(255) NOT NULL, 
   -- firstName varchar(255) DEFAULT NULL,
   -- lastName varchar(255) DEFAULT NULL,
   -- gender ENUM('male', 'female') NOT NULL,
   -- dob DATE DEFAULT NULL,
   -- moduleCode VARCHAR(255) DEFAULT NULL,
   PRIMARY KEY (studentID)
   -- CONSTRAINT FK_ModuleStudent
   -- FOREIGN KEY (moduleCode) REFERENCES modules(moduleCode)
   -- ON DELETE RESTRICT
   );    



INSERT INTO students (email, password, firstName, lastName, gender, dob) VALUES ("john.doe@mail.com", "zxcv", "John", "Doe", "male", "2006-08-23");
INSERT INTO students (email, password, firstName, lastName, gender, dob) VALUES ("mary.gil@mail.com", "asdf", "Mary", "Gilmore", "female", "2003-03-15");

INSERT INTO modules (moduleCode, moduleName, location, credits) 
VALUES 
("CS6405 ", "Datamining", "Dublin", 5),
("CS6421 ", "Deep Learning", "Cork", 5),
("CS6408  ", "Database Technology", "Cork", 5),
("CS6461 ", "Machine Learning and Statistical Analytics", "Galway", 10),
("CS6322 ", "Optimisation", "Sligo", 5),
("CS6420 ", "Topics in Artificial Intelligence ", "Galway", 10),
("CS6422 ", "Complex Systems Development ", "Dublin", 10);

drop table students;