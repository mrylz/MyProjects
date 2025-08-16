isimler = ["ali","mert","ada","akif","mehmet"]
x  = list(filter(lambda isim : isim[0] == "a",isimler))
print(x) # -> Bu şekilde isimler listesindeki her a harfi ile başlayan isim filtreledik
y = list(map(lambda isim : isim.upper(),x))
print(y) # -> Bu kod parçası ile filtreleme yaptığımız kod parçasını map ile birlikte harflerini büyüttük
users = [
    {"username" : "mehmet yılmaz" , "posts" : ["post1","post2"]},
    {"username" : "murat yılmaz" , "posts" : ["post1","post2","post3"]},
    {"username" : "adil yılmaz" , "posts" : ["post2"]},
    {"username" : "mert yılmaz" , "posts" : []}
]
sonuc = list(filter(lambda x : len(x["posts"]) != 0,users)) # -> verilen dict yapısı içindeki postu olanları  filtreler
isim = list(map(lambda x : x["username"],sonuc)) # -> filtrelediğimiz  bilgiler içindeki username bilgisini bize getirir
son = [i["username"] for i in users if len(i["posts"]) > 0] # -> yukarıda 2 satırda yaptığımz işlemi tek satırda da yapabilirz
print(sonuc)
print(isim)
print(son)