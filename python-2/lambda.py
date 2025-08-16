# lambda argument : epression
kareAl = lambda a: a ** 2
print(kareAl(5))
# lambda bizde fonksiyon kolaylığı sağlayabilir bir fonksiyon ile yazacağımız uzun satırları kısaltabilir.
# Bazı durumlarda fonksiyonun yerini alabilir
sayi = int(input("Lütfen  karesi alınacak sayıyı  giriniz : "))
sonuc = (lambda a: a ** 2)(sayi)
print("Kare : " + str(sonuc))
