import csv
with open("personality_dataset.csv") as file:
    sonuc =  csv.reader(file)
    liste = list(sonuc)
    print(liste[1])
    # bu programda elimizdeki bir csv dosasının içindeki verileri okumayı öğrendik 
    # ve bu verilderden istediğimiz gibi kullanmayıda öğrenebliriz
    