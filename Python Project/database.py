import random
import pymysql as pyms
import bcrypt
import requests





class Database:
    def __init__(self):
        self.connection = pyms.connect(host="127.0.0.1", port=3306, user="root", password="", database="gta_bank")
        print("Database connected")

        self.cursor = self.connection.cursor()
        print("Cursor connected")
        
        self.bank_lists = null
        try:
            self.cursor.execute("CREATE DATABASE gta_bank")
            print("Database created")
        except Exception as e:
            print(e)
        
        try:
            self.cursor.execute("CREATE TABLE users(id INT AUTO_INCREMENT PRIMARY KEY, balance INT, account_number VARCHAR(11), first_name VARCHAR(25) NOT NULL, last_name VARCHAR(25), email VARCHAR(35) NOT NULL UNIQUE, password VARCHAR(225) NOT NULL, pin VARCHAR(225) NOT NULL)")
            print("Tables created")
        except Exception as e:
            print(e)
        
        
    def create_account(self, first_name: str, last_name: str, email: str, password: str, pin: str)->tuple[bool, str, str]:
        """"
        A database function to execute account creation and save to the database
        """
        
        try:
            query = "INSERT INTO users(first_name, last_name, email, password, pin, balance, account_number) VALUES(%s,%s,%s,%s,%s,0,%s)"
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            hashed_pin = bcrypt.hashpw(pin.encode('utf-8'), bcrypt.gensalt())
            account_number = random.randint(1, 9999999999)

            values = (first_name, last_name, email, hashed_password, hashed_pin, account_number)
            self.cursor.execute(query, values)
            self.connection.commit()
            
            
        
            print("Account created")
            return (True, "Successful", account_number)
        except Exception as e:
            print(e)
            if e.args[0] == 1062:
                return (False, "Email already exists", None)
            elif e.args[1]:
                return (False, e[1], None)
            else:
                return (False, "Something went wrong", None)
                
    def login(self, account_number: str, pin: str)->tuple[bool, str|dict]:
        """"
        A database function to execute fetching and authentication process
        """
        
        try:
            query = "SELECT * FROM users WHERE account_number=%s"
            value = (account_number)
            self.cursor.execute(query=query, value=value)
            user_details = self.cursor.fetchone()
            if not user_details:
              return (False, "No account found")
          
            is_pin_correct = bcrypt.checkpw(pin.encode("utf-8"), user_details.pin)
            if not is_pin_correct:
              return (False, "Incorrect pin", None)           
        
            print("Login Successful")
            return (True, "Successful", user_details)
        except Exception as e:
            print(e)
            return (False, "Something went wrong", None)
                
    def fetch_bank_list(self):
        if self.bank_lists:
            return self.bank_lists
        
        json_res = requests.get("https://jsonplaceholder.typicode.com/comments")
        lists = json_res.json()
        self.bank_lists = lists
        return lists