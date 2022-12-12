# import module and database access configuration file
import mysql.connector
import config as cfg

# Class object for Database Access Object (DAO)
class CollegeDAO:
    '''
    connection=''
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
'''
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

        '''
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
            
            
        '''
        self.cursor = self.connection.cursor()
        return self.cursor
    '''    
    def initConnectToDB(self):
      db = mysql.connector.connect(
         host=cfg.mysql['host'],
         user=cfg.mysql['username'],
         password=cfg.mysql['password'],
         database=cfg.mysql['database'],
         pool_name='my_connection_pool',
         pool_size=5
      )
      return db
    '''
    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    # Return user info based on email and password
    def verify(self, data):
        cursor = self.getcursor()
        sql = 'SELECT * FROM students WHERE email = %s and password = %s'
        #values = [
        #    data['email'],
        #    data['password']
        #]
        #values =[data['email'], data['password']]
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
        #u = self.convertToDictionary(result)
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
        # return u['userID']

collegeDAO = CollegeDAO()

if __name__ == "__main__":
    print ('sanity')
    data = ['as@as.as', 'as']
    #data = {'email': 'as@as.as', 'password':'as'}
    collegeDAO.verify(data)