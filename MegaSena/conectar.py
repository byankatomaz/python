import mysql.connector

conexaomega = mysql.connector.connect(
    host='localhost',
    database='megasena',
    user='root',
    password=''
)

cursor = conexaomega.cursor()
cursor.execute('select database();')
cursor.fetchone()