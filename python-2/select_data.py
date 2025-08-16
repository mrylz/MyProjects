import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sade1234",
    database = "shopdb"
)
cursor = db.cursor()
# sql = "SELECT * FROM products" =>  Tüm bilgileri getiren sorgu
sql = "SELECT id,name FROM products" # => Sadece id ve name bilgisini getiren sorgu 
cursor.execute(sql)
sonuc = cursor.fetchall()
for i in sonuc:
    print(i)