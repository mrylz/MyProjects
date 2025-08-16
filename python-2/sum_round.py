products = [
    {"urunAdi" : "telefon" , "price" : 70000},
    {"urunAdi" : "Araba" , "price" : 80000},
    {"urunAdi" : "Radyo" , "price" : 90000},
    {"urunAdi" : "teflon" , "price" : 100000}
]
sonuc = sum([urun["price"] for urun in products])
print(sonuc) # sum fonk. verilen değerleri toplama işlemi yapar
boyut = len(products)
print(sonuc/boyut) # Bu şekilde fiyat ortalamasını alabiliriz
print(round(3.23)) # -> Yuvarlama işlemini yapar
print(round(3.464,2)) # -> Yuvarlama işlemini yaparken virgülden sonraki basamka  sayısını bu şeilde gösterebiliriz