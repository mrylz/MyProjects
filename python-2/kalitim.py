class Person: # person sınıfı oluşturuldu
    def __init__(self,name,sname,age): # gerekli attributler alındı
        self.name = name
        self.sname = sname
        self.age = age
    def  intro(self): # person sınıfı altında diğer bir method tanımlandı  endini tanıtmak için
        print(self.name,self.sname,self.age)
class student(Person): # person sınıfından kalıtım alınarak student sınıfı oluşturuldu
    pass
class teacher(Person): # person sınıfından kalıtım alınarak teacher sınıfı oluşturuldu
    pass        


p1 = Person("ali","yılmaz",27) # person sınıfı basıldı
p1.intro() 
s1 = student("mert","boz",12) # student sınıfı basıldı
s1.intro()
t1 = teacher("mehmet","bozos",32) # teacher sınıfı basıldı
t1.intro()