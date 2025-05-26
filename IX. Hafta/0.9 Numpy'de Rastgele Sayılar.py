#Numpy'de Rastgele Sayılar

"""
Rastgele: Tahmin edilemeyen sayı.

Bilgisayarlar algoritmalarla çalışır, yani üretilen sayılar aslında tamamen rastgele değil, sözde rastgeledir.

NumPy, bu sözde rastgele sayıları üretmek için random modülünü sunar.
"""

from numpy import random

#randint ifadesi 0 dan belirlenen sayılardan rastgele değer üretir.
x = random.randint(100)  # 0-99 arası bir sayı
print(x)

#rand ifadesi ise float türünde  0.0 - 1.0 arasında sayı üretir.
x = random.rand()
print(x)



#Rastgele dizi üretimi
x = random.randint(100, size=5)      # 5 elemanlı 1D dizi
x = random.randint(100, size=(3, 5)) # 3x5 boyutlu 2D dizi
print(x)

#Float sayıları ile:
y = random.rand(5)       # 5 elemanlı 1D float dizi
x = random.rand(3, 5)    # 3x5 boyutlu 2D float dizi
print(x)


#Diziden rastgele seçme
x = random.choice([3, 5, 7, 9])
print(x)
#choice() yöntemi ayrıca bir dizi değer döndürmenize olanak tanır.

# Belirli elemanlardan oluşan rastgele dizi
x = random.choice([3, 5, 7, 9], size=(3, 5))  # 3x5 boyutlu dizi
print(x)

"""
random.randint(n)	0-n arası rastgele tamsayı üretir
random.rand()	0-1 arası rastgele float üretir
random.randint(n, size=(x, y))	Boyutlu rastgele int dizisi üretir
random.rand(x, y)	Boyutlu rastgele float dizisi üretir
random.choice([...])	Listeden rastgele tek bir değer seçer
random.choice([...], size=(x,y))	Belirli değerlerden oluşan rastgele dizi
"""
