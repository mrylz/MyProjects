# -> Genel Yapısı : x = [expression  for i in liste ]
sayilar = []
for i in range(5):     # -> 3 satırda yazılan bu kod parçasını 
    sayilar.append(i)
print(sayilar)
sayilar2 = [i for i in range(5)] # -> 1 satıra  indirgeyen kod parçası
print(sayilar2)
kurum = "Btk Akademi"
sonuc = [i.upper() for i in kurum] # -> upper() ile harfleri büyük harfe  çevirme işlemi  
print(sonuc)
