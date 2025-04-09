"""
Fonkisyon oluşturmak için
"""

def deger():
    print("Fonksiyon Merhaba ! ")

deger()

"""
Daha işlevsel olacak olursa:
"""

def isim(isim):
    print(isim + " Gül")
isim("Furkan")
isim("Adnan")

"""
Ne kadar argüman ekleneceği belliyse argüman sayısı yazılır.
"""

def isimsoyisim(isim1, soyisim):
    print(isim1 + " " + soyisim)

isimsoyisim("furkan","gül")

"""
Ne kadar argüman ekleneceği belli değilse * işareti kullanılır.
"""

def fonk(*cocuklar):
    print("en genç çocuk:" + cocuklar[0])

fonk("berat", "kerem", "ihsan")


"""
Ayrıca anahtar = değer sözdizimi ile bağımsız değişkenler gönderebilirsiniz.
Bu şekilde argümanların sırası önemli değildir.
"""

def al(sim,esim,desim):
    print(esim)
al(esim="deger", desim="değmez", sim="mevcut")

"""
Fonksiyonunuza kaç tane anahtar kelime argümanının iletileceğini bilmiyorsanız, fonksiyon
tanımında parametre adından önce iki yıldız işareti ekleyin: **.
Bu şekilde fonksiyon bir argüman sözlüğü alacak ve buna göre öğelere erişebilecek:
"""

def fonksiyonum(**cocuk):
 print("Soyismi " + cocuk["soyisim"])
fonksiyonum(soyisim="kılca")


"""
Argümansız çağırırsak hata alamamak için değer atarız
"""

def ulkem(cont = "Turkey"):
    print("My Contry: " + cont)

ulkem()
ulkem("Sweden")

"""
 Argüman olarak bir Liste gönderirseniz, işleve ulaştığında hala bir Liste olacaktır:
"""

def fonksiyonum(meyve):
    for x in meyve:
        print(x)
meyve = ["elma", "muz", "kiraz"]
fonksiyonum(meyve)


"""
Bir fonksiyonun bir değer döndürmesine izin vermek için return ifadesini kullanın:
"""


def hesapla(x):
    return x * 5 + 2
print(hesapla(3))

"""
Fonksiyon tanımları boş olamaz, ancak herhangi bir nedenle içeriği olmayan bir fonksiyon
tanımınız varsa, hata almamak için pass ifadesini girin.
"""

def fonksyonum():
 pass

fonksyonum()

"""
Özyineleme Rekürisif Fonk.
"""

"""
Python ayrıca fonksiyon özyinelemesini de kabul eder; bu, tanımlanmış bir fonksiyonun
kendisini çağırabileceği anlamına gelir
"""

def ozyineleme(k):
    if(k > 0):
        sonuc = k + ozyineleme(k - 1)
        print(sonuc)
    else:
        sonuc = 0
    return sonuc
print("\n\n Özyineleme Örneği Sonuçları ")
ozyineleme(6)
"""
lambda, tek satırlık fonksiyonlardır.
"""

x = lambda a : a+2
print(x(2))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


"""
Lambda'nın gücü, onları başka bir fonksiyonun içinde anonim bir işlev olarak kullandığınızda
daha iyi gösterilir.
"""

"""
Fonksiyonu 2 ye katlamak istersek
"""
def fonksiyonum(n):
    return lambda a : a * n
iki_katlama = fonksiyonum(2)


"""
3e katlamak istersek
"""
def fonksiyonum(n):
     return lambda a : a * n
uce_katlama = fonksiyonum(3)
print(uce_katlama(11))
