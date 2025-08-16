def selamalama(fn):
    def inner():
        print("hoşgeldiniz")
        fn()
        print("görüşmek üzere")
    return inner
def günaydin():
    print("günaydın")
def iyigünler():
    print("iyi günler")

g = selamalama(günaydin)    
g() # günaydın fonk. çalıştırarak için blokları işleme alır.          
i = selamalama(iyigünler)
i() # iyigünler fonk. çalıştırarak içindeki blokları işleme alır.
def selamalama(fn):
    def inner():
        print("hoşgeldiniz")
        fn()
        print("görüşmek üzere")
    return inner
@ selamalama
def günaydin():
    print("günaydın")
@ selamalama
def iyigünler(): 
    print("iyi günler")

günaydin()
iyigünler() # -> yukarıda decoration ile selamalama fonk.içeri dahil ettiğimiz için tekrardan gerek duymuyoruz