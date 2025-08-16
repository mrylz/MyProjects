class Person: # person sınıfı oluşturuldu
    def __init__(self,name,sname,age): # gerekli attributler alındı
        self.name = name
        self.sname = sname
        self.age = age
    def  intro(self): # person sınıfı altında diğer bir method tanımlandı  endini tanıtmak için
        print(self.name,self.sname,self.age)
class student(Person): # person sınıfından kalıtım alınarak student sınıfı oluşturuldu
    def __init__(self,name,sname,age,number): # kendi init fonk. number gibi bi eklenti daha almış olduk
        super().__init__(name,sname,age) # Bu sayede person sınıfının init fonk. çalıştırmış oluruz
        self.number = number # burada numbe kısmını halletmiş olduk
    def  intro(self): # Yukarıdaki intro methodunu kırarak kendi methodmuza eklentiler yapmış olduk
        print(self.name,self.sname,self.age,self.number)
    def study(self):
        print(f"{self.name} ders çalışıyor")    
class teacher(Person): # person sınıfından kalıtım alınarak teacher sınıfı oluşturuldu
    def __init__(self,name,sname,age,branch):
        super().__init__(name,sname,age)
        self.branch = branch 
    def  intro(self): # person sınıfı altında diğer bir method tanımlandı  endini tanıtmak için
        print(self.name,self.sname,self.age,self.branch) 
    def teach(self): # diğer methodlardan farklı olarak kendı methodumuzuz tanımlamış olduk
        print(f"{self.name}{self.branch} anlatıyor")         
         


p1 = Person("ali","yılmaz",27) # person sınıfı basıldı
p1.intro() 
s1 = student("mert","boz",12,309) # student sınıfı basıldı
s1.intro()
s1.study()
t1 = teacher("mehmet","bozos",32,"fizik") # teacher sınıfı basıldı
t1.intro()
t1.teach()