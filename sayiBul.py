import random
sayi = random.randint(1,100)
while(True):
    kosul = int(input("Sayı : "))
    if(kosul > sayi):
        print("lütfen daha küçük bir sayı giriniz")
    elif(sayi > kosul):
        print("lütfen daha büyük bir sayı giriniz")
    else:
        print("Tebrikler  doğru sonucu buldunuz")
        break

