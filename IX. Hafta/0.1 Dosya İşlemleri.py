#Dosya İşlemleri

#Python da dosyaları çalıştırmak için temel olarak open() fonksiyonu kullanılmaktadır.

#Dosya açmak için:

f = open("liste.txt")
f.close()
#Veya
g = open("liste.txt", "rt")
g.close()

"""
open() fonksiyonu open("uzantı", "mod") şeklinde çalışır.
mod kısmına dosyanın ne yapacağı belirtilir.

modlar:

'r' -> Dosya okumak için kullanılır. Varsayılan moddur. Dosya yoksa hata verir.

'w' -> Dosyayı yazmak için kullanılır. Dosya yoksa oluşturulur. Varsa içeriğini siler.

'a' -> Append kelimesinden gelir. Var olan içeriğini silmeden dosyaya yeni şeyler ekler. Dosya yoksa dosyayı oluşturur.

'x' -> Dosyayı yeni oluşturur. Zaten dosya var ise hata verir.


Dosyayı normal yazı formatında mı yoksa binary formatında mı açacağımızı belirtmek için:

't' -> Text yani yazı formatında dosyayı açmamızı sağlar. Dosya içeriğini metin olarak işler. Varsayılan moddur.

'b' -> Dosya içeriğini ham ikilik veri olarak işler. ( Örnek olarak resim, müzik dosyalarını) 


Kombinasyonlar :


'rt' -> Okuma + Metin Formatında

'rb' -> Okuma + Binary Formatta

'wt' -> Yazma + Metin Formatında 

'wb' -> Yazma + Binary Formatta

'at' -> Ekleme + Metin Formatında

'ab' -> Ekleme + Binary Formatta
"""


#Dosya okuma için
f1 = open("liste.txt" , "r")
print(f1.read())
f1.close()

#Dosya yazmak için
f2 = open("liste.txt", "w")
f2.write("Ahmet")
f2.close()

#Dosya eklemek için
f3 = open("liste.txt", "a")
f3.write("Cemal")
f3.close()

#Dosya oluşturmak için.
f4 = open("yeni_dosya_olustur.txt", "x")
f4.write("Yeni Dosya Olusturuldu !")
f4.close()



"""
yaptığımız dosya işlemlerinden sonra mutlaka close() fonksiyonu ile dosyayı kapatmamız gerekmektedir. !
"""

#Dosya silme işlemleri

"""
Python da dosyaları silmek için os kütüphanesi kullanılmaktadır. 
os kütüphanesi zaten IDE lerde otomatik olarak ekli gelmektedir.
"""

import os
#Mesela bir dosyayı silmek istersek remove() fonkisyonu ile bunu gerçekleştirebiliriz.
os.remove("yenidosya.txt")


#Var olmayan bir dosyayı silmeye çalışırsak hatalar ile karşılaşabiliriz. Bunun için dosyanın olup olmadığını kontrol etmemiz gerekmektedir.
#Kontrol etmek için os kütüphanesi ile gelen path.exist() fonksiyonu kullanılmaktadır.
if os.path.exists("yenidosya.txt"):
    os.remove("yenidosya.txt")
else:
    print("dosya mevcut değildir !")

#Komple dosya kaldırmak istersek rmdir() komutu kullanılmaktadır.
os.rmdir("Dosyam")
