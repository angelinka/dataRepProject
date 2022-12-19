# import module and database access configuration file
import mysql.connector
import config as cfg

# Class object for Database Access Object (DAO)
class CollegeDAO:
 
    # Create database connection pool
    def __init__(self):
        host=cfg.mysql['host']
        user=cfg.mysql['username']
        password=cfg.mysql['password']
        database=cfg.mysql['database']
         #pool_name='my_connection_pool',
         #pool_size=5
    
    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['username'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database']
            
            )
        self.cursor = self.connection.cursor()
        return self.cursor
   
    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    # Return user info based on email and password
    def verify(self, data):
        cursor = self.getcursor()
        sql = 'SELECT * FROM students WHERE email = %s and password = %s'
        values = data
        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        u = self.convertToDictionary(result)
        return u

    def convertToDictionary(self, result):
        colnames=['studentID','email','password', "firstname", "lastname", "gender", "dob"]
        item = {}
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        return item
    
    def checkEmail(self, check):
        cursor = self.getcursor()
        sql = 'SELECT * FROM students WHERE email = %s'
        values = check
        cursor.execute(sql, values)
        result = cursor.fetchone()
        print(result)
        self.closeAll()
        return result

     # Create user, returns userID of new user
    def createStudent(self, data):
        cursor = self.getcursor()
        sql = "insert into students ( email, password, firstname, lastname, gender, dob) VALUES ( %s,  %s,  %s, %s, %s, %s) "
        values = data
        cursor.execute(sql, values)
        self.connection.commit()
        lastRowId = cursor.lastrowid
        self.closeAll()
        return lastRowId
      

         # Create module, returns moduleCode of new module
    def createMod(self, mod):
        cursor = self.getcursor()
        sql = "insert into modules (moduleCode, moduleName, location, credits) values (%s, %s, %s, %s)"
        values = [
        mod['moduleCode'], 
        mod['moduleName'],
        mod['location'],
        mod['credits']
        ]
        cursor.execute(sql, values)
        self.connection.commit()
        lastRowId = cursor.lastrowid
        self.closeAll()
        return lastRowId


     # Return info on all modules
    def getAllMod(self):
        cursor = self.getcursor()
        sql = 'select * from modules'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        # print(results)
        for result in results:
           resultAsDict = self.convertModToDict(result)
           returnArray.append(resultAsDict)
        self.closeAll()
        return returnArray

      
          # Return info on module for given moduleCode
    def findModById(self, moduleCode):
        cursor = self.getcursor()
        sql = 'select * from modules where moduleCode = %s'
        values = [moduleCode]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        module = self.convertModToDict(result)
        self.closeAll()
        return module


    # Update module info for given moduleCode, returns updated info
    def updateMod(self, mod):
        cursor = self.getcursor()
        sql = "update modules set moduleName = %s, location = %s, credits = %s where moduleCode = %s"
        values = [
         mod['moduleName'],
         mod['location'],
         mod['credits'],
         mod['moduleCode']
      ]   
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        return mod

    # Delete module for given moduleCode, returns empty dictionary/JSON
    def deleteMod(self, mod):
        cursor = self.getcursor()
        sql = 'delete from modules where moduleCode = %s'
        values = [mod]
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        return {}

     # Function to convert module into Dictionary/JSON
    def convertModToDict(self, result):
        colnames = ['moduleCode', 'moduleName', 'location', 'credits']
        mod = {}
        if result:
           for i, colName in enumerate(colnames):
              value = result[i]
              mod[colName] = value
        return mod

collegeDAO = CollegeDAO()

if __name__ == "__main__":
    print ('sanity')
    data = ['as@as.as', 'as']
    #data = {'email': 'as@as.as', 'password':'as'}
    collegeDAO.verify(data)