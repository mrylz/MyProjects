import csv
with open("personality_dataset.csv") as file:
    sonuc = csv.DictReader(file)
    for i in sonuc:
        if i["Stage_fear"] == "yes":
            print(i["Time_spent_Alone"],i["Stage_fear"])
            # bu kısımda da bi csv dosyasını dict veri yapısı ile kontrol edebilmeyi öğrendik