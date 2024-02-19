import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'AnsariMd754'
)

# preparing cursor object

cursor_object = database.cursor()

# creating database

cursor_object.execute("CREATE DATABASE crm_datas")
print("Database created Successfully")