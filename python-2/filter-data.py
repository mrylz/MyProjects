import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sade1234",
    database = "shopdb"
)
cursor = db.cursor()
# sql = "SELECT * from products WHERE id>1" => id 1'den büyük olanları getirir
# sql = "SELECT * from products WHERE name LIKE 'Samsung' "# => LIKE ile aradaki istenilen kelmeye bakıyoruz.

id = input("İD : ")
sql = "SELECT * from products WHERE id = %s"
params = (id,)

cursor.execute(sql,params)
result = cursor.fetchall()
print(result)
