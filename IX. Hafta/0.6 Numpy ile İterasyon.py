#Numpy ile İterasyon

"""
Yineleme (iterasyon), bir dizi içindeki öğelerden tek tek geçmek anlamına gelir.
NumPy ile çalışırken çok boyutlu diziler üzerinde de bu işlemleri yapabiliriz.
"""
import numpy as np

#1. Boyutta iterasyon için:
bir =  np.array([1, 2, 3])
print("Birinci Boyut Elemanları:")
for x in bir:
    print(x)

#2. Boyutta iterasyon için:
iki = np.array([[1, 2, 3], [4, 5, 6]])
print("\nİkinci Boyut Elemanları:")
for x in iki:
    for y in x:
        print(y)

#3. Boyutta iterasyon için:
uc = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("\nÜçüncü Boyut Elemanları:")
for x in uc:
    for y in x:
        for z in y:
            print(z)

#For döngüler ile uğraşmak yerin nditer() fonksiyonu ile skaler bir şekilde bize elemanları vermektedir.
print("\nSkaler bir şekilde sıralama için:")
for x in np.nditer(uc):
    print(x)


#Veri tipini değiştirerek iterasyon oluşturacaksak:
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)
#kodda op_dytype ifadesi string veriye çevirmeyi sağlar.
# flags=['buffered'] ifadesi ise numpy bellek üzerinde bu işlemi yapamadığından geçici olarak bize yer açar.


#Farklı şekillerde iterasyon için:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
    print(x)
#[:,::2]ifadesinde ilk : tüm satırları alamamızı ister. diğer satır ise ikişer ikişer almamızı sağlar.


#np.ndenumerate() fonksiyonu ile iterasyonları numaralandırabiliriz.
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
    print(idx, x)

#ikinci dizi için:
arr = np.array([[1, 2], [3, 4]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)

