import mysql.connector

conexaomagazine = mysql.connector.connect(
    host='localhost',
    database='celulares',
    user='root',
    password=''
)

cursor = conexaomagazine.cursor()
cursor.execute('select database();')
cursor.fetchone()