#Python'da Veri Tipleri
import numpy as np
"""
Python'da değişkenlerin bir veri türü (data type) vardır ve bu tür, değişkenin bellekte nasıl saklandığını belirler.
str ->	Metin
int ->	Tamsayı
float ->	Ondalıklı sayı
bool -> Mantıksal değer
complex ->	Karmaşık sayı
"""

"""
Numpy kütüphanesinde ise Pythondaki veri tiplerine ek olarak daha fazla veri türü desteklenmektedir. Ve bu türler kısaltmalar ile ifade edilir.

i -> int -> tam sayılar için 
u -> unsigned int -> işaretsiz tamsayı
f -> float -> ondalıklı sayı
c -> complex -> karmaşık sayı
b -> bool -> mantıksal ifadeler
S -> bytes string -> sabit uzunluktaki diziler
U -> uncode string -> unicode dize
O -> object -> python nesnesi
M -> datetime64 -> tarih zaman 
m -> timedelta64 -> zaman farkı 
v -> void -> sabit bellekteki alan
"""

#dtype parametresi ile dizinin türünü bulabilmekteyiz.
intdizisi = np.array([1,2,3,4,5])
stringdizi = np.array(['elma', 'muz', 'kiraz'])
print(intdizisi.dtype)
print(stringdizi.dtype) #U5 çıkar o da unicode dizisi anlamındadır.
print()


#dtype ile dizinin türünü belirleyebiliriz.
arr = np.array([1, 2, 3], dtype='S')  # S = byte string
print(arr)
print(arr.dtype)  # |S1 veya |Sx


print()
arr = np.array([1, 2, 3], dtype='i4')
print(arr)
print(arr.dtype)  # int32

#Hatalı durumlarda yani dizi ile veri tipi uyuşmaz ise hata mesajı alınmaktadır.
print()
#arr = np.array(['a', '2', '3'], dtype='i')
# ValueError: invalid literal for int() with base 10: 'a'



#Var olan dizinin türünü değiştirmek için astype() fonksiyonu kullanılmaktadır.

dizi = np.array([1.5, 2.8, 4.8])
yeni_Dizi = dizi.astype("i")
print(yeni_Dizi)
print(yeni_Dizi.dtype)




dizi1 = np.array([1, 0, 3])
new_arr = dizi1.astype(bool)
print(new_arr)        # [ True False  True ]
print(new_arr.dtype)  # bool



"""
Numpy kütüphanesinde astype ile dtype bakacak olursak:

dtype: dizi türünü öğrenmeye yarar
astype: türü değiştirir.

dtype: orjinal diziyi değiştiremez.
astype: orjinal diziyi değiştiremez.

kullanımı: 
dizi.dtype
dizi.astype("yeni_Veri_tipi") 
"""
