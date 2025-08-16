# Genel Yapısı : x = [expression for i in item if kosul]
# Genel Yapısı : x = [expression if kosul else çıktı for i  in item if kosul ]
sayilar = [1,5,67,78,95,34,68,23,97,96,54]
sayilar2 = []
for sayi in sayilar:
    if sayi %  2  == 0:
        sayilar2.append(sayi) # -> bu ekleme işlemini  
print(sayilar2)        

sayilar3 = [24,26,35,4,86,90,80,56]
sayilar4 = [i for i in sayilar3 if i % 2 == 0] # -> Tek Satırda yapmamızı sağlar
print(sayilar4)

sayilar5 = [24,26,35,4,86,90,80,56]
sayilar6 = [i if i %  2 == 0 else "Tek sayıdır" for i in sayilar3] # -> Tek Satırda yapmamızı sağlar
print(sayilar6)
