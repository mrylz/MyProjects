islem = str(input("İşlem(+,-,*,/) = "))
sayi1= int(input("1.Sayı = "))
sayi2= int(input("2.Sayı = "))
if islem == "+":
    print("Sonuç :  " + str(sayi1 + sayi2) )
elif islem == "-":
    print("Sonuç :  " + str(sayi1 - sayi2) )
elif islem == "/":
    print("Sonuç :  " + str(sayi1 / sayi2) )
elif islem == "*":
    print("Sonuç :  " + str(sayi1 * sayi2) )
else:
    print("Yanlış  bi işlem  yaptınız") 

