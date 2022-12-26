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
   firstname varchar(255) NOT NULL,
   lastname varchar(255) NOT NULL,
   gender ENUM('male', 'female') NOT NULL,
   dob DATE DEFAULT NULL,
   PRIMARY KEY (studentID)
   );    

CREATE TABLE IF NOT EXISTS enrolment(
	studentID INT NOT NULL,
    moduleCode VARCHAR(255) NOT NULL,
    PRIMARY KEY (studentID, moduleCode),
    FOREIGN KEY (studentID) REFERENCES students(studentID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (moduleCode) REFERENCES modules(moduleCode) ON DELETE CASCADE ON UPDATE CASCADE	
);

INSERT INTO students (email, password, firstname, lastname, gender, dob) VALUES ("john.doe@mail.com", "zxcv", "John", "Doe", "male", "2006-08-23");
INSERT INTO students (email, password, firstname, lastname, gender, dob) VALUES ("mary.gil@mail.com", "asdf", "Mary", "Gilmore", "female", "2003-03-15");

INSERT INTO modules (moduleCode, moduleName, location, credits) 
VALUES 
("CS6405", "Datamining", "Dublin", 5),
("CS6421", "Deep Learning", "Cork", 5),
("CS6408", "Database Technology", "Cork", 5),
("CS6461", "Machine Learning and Statistical Analytics", "Galway", 10),
("CS6322", "Optimisation", "Sligo", 5),
("CS6420", "Topics in Artificial Intelligence", "Galway", 10),
("CS6422", "Complex Systems Development", "Dublin", 10);

INSERT INTO enrolment (studentID, moduleCode) VALUES
(1, "CS6461"), 
(1, "CS6420"),
(2, "CS6461");

drop table modules;
drop table enrolment;
select * from students;
select * from modules;
select * from enrolment;

select m.moduleCode, m.moduleName, m.location, m.credits
from modules m
join enrolment e on m.moduleCode = e.moduleCode
join students s on (e.studentID = s.studentID)
where e.studentID = 1;