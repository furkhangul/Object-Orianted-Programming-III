"""
Class Kullanımı
"""
from numpy.random.mtrand import permutation


class S:
    x=5
sinifim = S()
print(sinifim.x)

"""
init kullanımı 
"""

class Personel():
    def __init__(self,isim,soyisim,yas):
            self.isim = isim
            self.soyisim = soyisim
            self.yas = yas

p1 = Personel("Furkan", "Gül", "21")
print(p1.isim)
print(p1.soyisim)
print(p1.yas)

"""
__init__() işlevi, sınıf yeni bir nesne oluşturmak için her kullanıldığında otomatik olarak
çağrılır.
"""

class Kullanicilar:
    def __init__(abc, isim,soyisim):
        abc.isim = isim
        abc.soyisim = soyisim

    def fonksiyonum(obs):
        print("Benim adım :", obs.isim)
k1 = Kullanicilar("Furkan", "Gül")
print(k1.isim)
k1.fonksiyonum()

"""
Diğer faktörleri ayarlayabiliyoruz.
"""
k1.isim = "KEREM"

"""
p1 nesnesinden age özelliğini silin:
"""

del p1.yas

"""
Sınıfı boş tanımlayamıyoruz bundan dolayı pass kullanırız.
"""
class Bos:
    pass
