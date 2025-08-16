sayilar = [1,3,5,7,9]
print(min(sayilar)) # -> En küçük sayıyıyı veren fonk.
print(max(sayilar)) # -> En büyük sayıyıyı veren fonk.
harfler = ["a","b","c","d","e"]
print(min(harfler)) # -> harfler içinde aynı şekilde verebilir
print(max(harfler))
urunler = [
    {"urunAdi" : "Samsung" , "price" : 10000},
    {"urunAdi" : "Iphone" , "price" : 20000},
    {"urunAdi" : "Huawei" , "price" : 30000}
]
sonuc = min(urunler,key = lambda a : a["price"])
print(sonuc) # -> en ucuz fiyatlı olanı gösterir.
sonuc = max(urunler,key = lambda a : a["price"])["urunAdi"]  
print(sonuc) # -> en yüksek fiyatlının urunAdi'ni gösterir.
