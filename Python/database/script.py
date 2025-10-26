import pymysql as pyms
import mysql.connector as msc
import random

my_con = pyms.connect(host="127.0.0.1", port=3306, user="root", passwd="", db="python_db_class")

# print(my_con)
print("Connection successful")

my_cursor = my_con.cursor()
print("Cursor connected")

# my_cursor.execute("CREATE DATABASE python_db_class")
# print("python_db_class database created successfully")

# my_cursor.execute("CREATE TABLE pupil_tb(pupil_id INT(3), first_name VARCHAR(20), last_name VARCHAR(20), email VARCHAR(50))")
# print("Table created successfully")


"""
DISPLAY ALL DATABASE
"""
# my_cursor.execute("SHOW DATABASES ")
# databases = my_cursor.fetchall()
# for db in databases[:5]:
#     print(db[0])
# my_cursor.close()


"""
DISPLAY ALL COLUMNS FROM A TABLE
"""
# my_cursor.execute("SHOW COLUMNS FROM pupil_tb")
# for col in my_cursor:
#     print(col)
# my_cursor.close()


# my_query = "ALTER TABLE pupil_tb MODIFY email VARCHAR(50) AFTER first_name"
# my_query = "ALTER TABLE pupil_tb MODIFY last_name VARCHAR(50) AFTER first_name"
# my_query = "ALTER TABLE pupil_tb CHANGE pupil_id student_id INT(5) PRIMARY KEY AUTO_INCREMENT"
# my_query = "ALTER TABLE pupil_tb ADD matric_no VARCHAR(10) UNIQUE"
# my_cursor.execute(my_query)

# print("Modified successfully")



"""
INSERTING DATA INTO A TABLE
"""

# my_query = "INSERT INTO pupil_tb(first_name, last_name, email) VALUES(%s,%s,%s)"
# vals=("Adegbite", "Joshua", "adegbite@gmail.com")
# my_cursor.execute(my_query, vals)
# my_con.commit()
# print(my_cursor.rowcount, "Records inserted successfully")
# my_cursor.close()

# for i in range(5):
#     first_name= input("Enter your first name: ")
#     last_name= input("Enter your last name: ")
#     email= input("Enter your email: ")
#     matric_number = "25" + str(random.randint(0000, 9999))
#     my_query = "INSERT INTO pupil_tb(first_name, last_name, email, matric_no) VALUES(%s,%s,%s,%s)"
#     vals=(first_name, last_name, email, matric_number)
#     my_cursor.execute(my_query, vals)
#     my_con.commit()

# print(my_cursor.rowcount, "Records inserted successfully")
# my_cursor.close()


    
# my_query = "SELECT * FROM pupil_tb"
# my_cursor.execute(my_query)
# for pupil in my_cursor:
#     print(pupil)

# my_query = "SELECT * FROM pupil_tb WHERE first_name=%s"
# val=("e")
# my_cursor.execute(my_query, val)
# for pupil in my_cursor:
#     print(pupil)

# my_query = "SELECT * FROM pupil_tb WHERE last_name LIKE '%e%'"
# my_cursor.execute(my_query)
# for pupil in my_cursor:
#     print(pupil)
    
# my_query = "SELECT * FROM pupil_tb"
# my_cursor.execute(my_query)
# row_count = my_cursor.rowcount
# print(f"Number of rows in your table pupil is: {row_count}")


    

# for i in range(100000):
#     print(random.randint(0000, 9999))



"""
TO UPDATE A DATA ON A TABLE
"""