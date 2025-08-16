import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sade1234",
    database = "shopdb"
)
cursor = db.cursor()

sql = "UPDATE products SET name = 'SAMSUNG S12',price = price * 1.2 WHERE id = 1"
cursor.execute(sql)
try:
    db.commit()
    print(f"{cursor.rowcount} tane kayıt güncellendi")
except:
    print("Bağlantınızı kontrol ediniz")    