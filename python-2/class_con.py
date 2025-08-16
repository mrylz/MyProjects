class CardItem:
    discoun_rate = 0.8
    item_count = 0 # bunun sınıf attribüte oldugunu gösterir.
    @classmethod # bunun sınıf methodu olduğunu gösterir.
    def display_item_discount(cls):
        return f"{cls.item_count} tane ürün oluşturuldu"
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity      # Bu şekilde bir sınıfın özelliklerini bir nesneye yüklemenin kısa yolunu gördük
        CardItem.item_count += 1
    def sepetiTopla(self):
        return self.price * self.quantity

    def indirimEkle(self):
        return  self.price * 0.8

item1 = CardItem("telefon",70000,2)
item2 = CardItem("bilgisayar",35000,1)
item3 = CardItem("Kitap",200,3)
print(item1.sepetiTopla())
print(item2.sepetiTopla())
print(item3.sepetiTopla()) # sepetteki ürünleri fiyatlarını adeti ile çarparak sepetin toplam fiyatına ulaşır
print(item1.indirimEkle()) # yüzde 20 indirim uygulanmış halini gösterir
print(CardItem.display_item_discount())


