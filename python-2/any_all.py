# all -> and gibi çalışır hepsinin True olması gereklidir
# any -> or gibi çalışır  biinin True olması True  cevap döndürmesi için yeterlidir
sayilar = [1,3,5,7,9,0]
sonuc = all([bool(sayi) for sayi in sayilar])
net = any([sayi for sayi in sayilar ])
print(sonuc) # -> Sayılar listesinden 0 dan büyük değerlere bakar hepsi 0'dan büyük olmadığı için False değer verir.
print(net) # -> Sayılar listesinden 0 dan büyük değerlere bakar biri 0'dan büyük olduğu için True değer verir.
users =["ali","çınar","ada"]
x = any([y[0] == 'a' for y in users])
print(x) # -> any fonk.olduğu için bir tanesinin a harfi ile başlaması True değer üretiyor
x = all([y[0] == 'a' for y in users])
print(x) # -> all fonk. olduğu için hepsi a harfi ile başlamalıydı o yüzden False değer üretiyor
