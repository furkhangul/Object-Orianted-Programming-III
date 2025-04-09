"""
***Yineleyiciler***
"""
tuple_deger = ("Elma", "Armut", "Muz" ,"Kivi")
yenileyici =iter(tuple_deger)
print(next(yenileyici))
print(next(yenileyici))
print(next(yenileyici))
print(next(yenileyici))


"""
Karakter için de yapılabilir.
"""

karakter = "Furkan"
yenileyici = iter(karakter)
print(next(yenileyici))
print(next(yenileyici))
print(next(yenileyici))
print(next(yenileyici))
print(next(yenileyici))
print(next(yenileyici))


"""
Kendimiz oluşturmamız için:
"""

class Kendi:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
deger = Kendi()
yenileyici = iter(deger)

print(next(yenileyici))
print(next(yenileyici))
print(next(yenileyici))




