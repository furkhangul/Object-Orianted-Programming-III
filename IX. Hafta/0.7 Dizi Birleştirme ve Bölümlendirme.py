#Dizi Birleştirme ve Bölümlendirme

"""
Numpyde dizileri birleştirmek için concatenate() fonksiyonu kullanılmaktadır.
"""
import numpy as np

dizi1 = np.array([1,2,3])
dizi2 = np.array([4,5,6])
yenidizi = np.concatenate((dizi1,dizi2), axis=0)
#axis=0 satır boyunca alt alta axis=1 ise sütun boyunca yan yana

#Veya
dizi1 = np.array([[1, 2], [3, 4]])
dizi2 = np.array([[5, 6], [7, 8]])
np.concatenate((dizi1, dizi2), axis=1)
# [[1 2 5 6]
#  [3 4 7 8]]


#İki diziyi birleştirdikten sonra yeni boyut eklemek için stack() fonksiyonu kullanılır.
dizi1 = np.array([1, 2, 3])
dizi2 = np.array([4, 5, 6])
yeni = np.stack((dizi1,dizi2),axis=1)
print(yeni)

#hstack() satırlar boyunca yığmak için kullanılır.
dizi1 = np.array([1, 2, 3])
dizi2 = np.array([4, 5, 6])
dizi = np.hstack((dizi1, dizi2))
print(dizi)

# vstack() sütunlar boyunca yığmak için.
dizi1 = np.array([1, 2, 3])
dizi2 = np.array([4, 5, 6])
dizi = np.vstack((dizi1, dizi2))
print(dizi)

#dstack() sütunlar boyunca yığmak için.
dizi1 = np.array([1, 2, 3])
dizi2 = np.array([4, 5, 6])
dizi = np.dstack((dizi1, dizi2))
print(dizi)


"""
hstack(): Yatay istifleme (axis=1)

vstack(): Dikey istifleme (axis=0)

dstack(): Derinlik boyunca (axis=2)
"""

#Dizileri bölme işlemleri:
#array_split(): Diziyi parçalara böler
print()
dizi = np.array([1, 2, 3, 4, 5, 6])
dizi3 = np.array_split(dizi, 3)
print(dizi3)

#4 e bölmek için
dizi = np.array([1, 2, 3, 4, 5, 6])
dizi3 = np.array_split(dizi, 4)
print(dizi3)

#Split() fonksiyonu da yapılabilir ama yukarıdaki örnekteki gibi eşit bölme işlemi yapamadığımızdan array_list() kullanılır.

#2 boyutlu olarak bölmek için:
print()
dizi = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
yenidizi = np.array_split(dizi, 3)
print(yenidizi)


#Başka bir örnekte ise :

dizi = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12],
[13, 14, 15], [16, 17, 18]])
yenidizi = np.array_split(dizi, 3)
print(yenidizi)


"""
np.array_split(dizi, 3, axis=1)  # sütunlara göre
np.array_split(dizi, 3, axis=0)  # satırlara göre

hsplit(): Yatay (sütunlara göre)

vsplit(): Dikey (satırlara göre)

dsplit(): Derinlik boyunca
"""

dizi = np.array([[1, 2, 3], [4, 5, 6]])
print(np.hsplit(dizi, 3))


"""
Birleştirme	concatenate()	Dizi birleştirme
Yeni eksenle	stack()	Boyut artırarak istif
Yatay istifleme	hstack()	Yan yana
Dikey istifleme	vstack()	Alt alta
Derinlik istif	dstack()	Yeni derinlikte
Dizi bölme	array_split()	Parçalara ayırma (esnek)
Eşit bölme	split()	Eşit parçalara ayırma
Satır bölme	vsplit()	Dikey bölme
Sütun bölme	hsplit()	Yatay bölme
Derinlik bölme	dsplit()	Derinlik boyunca bölme
"""
