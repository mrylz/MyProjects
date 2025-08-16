import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sade1234",
    database = "shopdb"
)
cursor = db.cursor()
id = input("SİLİNECEK İD : ")
sql = "DELETE FROM products WHERE id = %s"
params = (id,)
cursor.execute(sql,params)
try:
    db.commit()
    print(f"{cursor.rowcount} tane kayıt silindi")
except:
    print("Bağlantı Hatası")
finally:
    cursor.close()
    db.close()
    print("Bağlantı Koparıldı")
            