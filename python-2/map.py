# Genel Yapısı : list(map(islem,islemin yapılacağı yer))
# map fonk.  özelliği giren ve çıktı sayısı  eşitliği vardır.
sayilar = [1,2,3,4,5,-6]
isimler = ["ali","zeynep","fatma"]
kisiler = [
    {"ad" : "mehmet" , "soyad" : "yılmaz"},
    {"ad" : "murat" , "soyad" : "demir"}
    ]
sonuc = list(map(lambda sayi : sayi ** 2,sayilar)) # -> lambda ve  map fonk. ile birlikte kare alan
deger = list(map(str.capitalize,isimler)) # -> strcapitalize metodu ile birlikte ilk harfleri büyük yapan kod
isim  = list(map(lambda kisi : kisi["ad"],kisiler)) # -> dict veri yapısının içerisinden belli bir veriyi çeken kod
print(sonuc)
print(deger)
print(isim)
