import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sade1234",
    database = "shopdb"
)
cursor = db.cursor()
cursor.execute("SHOW TABLES")
for i in cursor:
    print(i)
