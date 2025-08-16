kurslar =[
    {"kursAdi" : "web", "count" : 10000},
    {"kursAdi" : "python", "count" : 20000},
    {"kursAdi" : "js", "count" : 5000}
]

x = sorted(kurslar,key  = lambda a : a["count"],reverse=True)
print(x) # -> Count  bilgisine göre sıralama işlemi yapıyor 
y = list(map(lambda a : a["kursAdi"],x))
print(y) # -> Sorted ile yapılan sıralamanın sadece kursAdi ifadesi ile alınmasını sağlar. 
