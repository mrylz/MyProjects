import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sade1234",
    database = "shopdb"
)
cursor = db.cursor()
sql = "INSERT INTO products (name,price,imageurl,description) VALUES (%s,%s,%s,%s)"
values = [
    ("Samsung s14",4000,"6.jpg","güzel gibi bir telefondur"),
    ("Iphone X",4000,"6.jpg","güzel gibi bir telefondur")
    ]
# cursor.execute(sql,value)  tekli kayıtlarda value ile bbirlikte kullanılır.
cursor.executemany(sql,values)
try:
    db.commit()
    print(cursor.rowcount,"kayıt edildi")
    print(f"son eklenen kaydın id : {cursor.lastrowid + 1} ")
except:
    print("Bağlantı kaynaklı bir hata oluştu")
finally:
    cursor.close()
    db.close()
    print("Bağlantı Sonlandırıldı")        