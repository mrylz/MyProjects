sayilar = [i for i in range (1,100) if i % 12 == 0]
print(sayilar) # 1'den 100'e kadar  12'ye tam bölünen sayılar
text = "Hello World 12345 World"
sayilar2 = [i for i in text if i.isdigit()]
print(sayilar2) # Verilen  textin  içindeki sayıları ekrana yazdır
sicakliklar = [20,15,0,-2,-5]
havaDurumu =  [i if i >= 4 else "buzlanma tehlikesi var"   for i in sicakliklar]
print(havaDurumu) # Verilen  sıcaklıkar  içindeki değerlere göre yazdırma işlemi
ogrenciler = ["ali","ahmet","ayşe"]
notlar = [50,60,80]
liste = [(ogrenciler[i],notlar[i]) for i in range(0,len(ogrenciler)) if notlar[i] > 50]
print(liste) #  Verilen iki listedeki elemanı birleştiren ve 50 üzerindeki notu yazan program
liste_dict = { key:value for (key,value) in liste if value > 50}
print(liste_dict) # buda alternaif bir yol
sonuc = [(x,y) for x in range(3) for y in range(3)]
print(sonuc) # iç içe 2 tane döngüyü yazan compherission