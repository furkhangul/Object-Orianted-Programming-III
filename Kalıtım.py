
class Kalitim:
    def __init__(self,isim,soyisim):
        self.isim = isim
        self.soyisim = soyisim
    def isimyazdir(self):
        print()

"""
Kalıtım için
"""
class student:
    def __init__(self,isim,soyisim):
        self.isim = isim
        self.soyisim = soyisim

class caliskanlar(student):
    def __init__(self,isim,soyisim,numara):
        student.__init__(self,isim,soyisim)
        self.numara = numara

s1 = student("Furkan","Gül")
c1 = caliskanlar("Furkan","Gül",1536)
print(c1.numara)



"""
Python ayrıca, alt sınıfın ebeveyninden tüm yöntemleri ve özellikleri miras almasını sağlayacak
bir super() işlevine sahiptir
"""

class person:
    def __init__(self,number,name):
        self.number = number
        self.name = name

class breaker(person):
    def __init__(self,number,name):
        super().__init__(number,name) #Self burada yok
    def hosgeldiniz(self):
        print(f"Merhaba hoş geldiniz {self.number} numaralı {self.name} adlı kullanıcı tarafından girşi yapıldı")
breaker1 = breaker(15, "Keven")
breaker1.hosgeldiniz()
print(breaker1.name)




