"""
[*] Pythonda değişik veri türleri vardır bunlar fakrlı amaçlar için kullanılır. Birkaç tanesini örnek olarak verecek olursak:
• Metin Türü: str
• Sayısal Türler: int, float, complex
• Sıra Türleri: list, tuple, range
• Eşleme Türü: dict
• Set Türleri: set, frozenset
• Boole Türü: bool
• İkili Türler: bytes, bytearray, memoryview
"""


"""
STR Kullanımı:
"""
x = "Merhaba Dünya ! "
print(x)

"""
INT Kullanımı:
"""
x = 15
print(x)

"""
Float Kullanımı:
"""

x = 12.5
print(x)


"""
Complex Kullanımı:
tek bir sütun konumunda birden fazla veri değerini temsil eden bir dönüşüm veri türüdür
"""

x = 1j
print(x)

"""
List Kullanımı:
herhangi bir sayıda diğer objeleri içinde bulunduran bir sandık vazifesi görüyor.
"""
x = ["ELMA", "ARMUT", "MUZ", 5]

print(x)

"""
Tuple Kullanımı: 
değişmez değer dizileri oluşturmanıza olanak tanıyan yerleşik bir veri türüdür.
Liste, öğelerin sıralı ve değiştirilebilir bir koleksiyonudur. Bir tuple, sıralı ve değiştirilemez bir öğe koleksiyonudur.
"""

x = ("Elma","Armut","Muz")
print(x)

"""
Range Kullanımı:
belirli kod blokları arasında belirtilen sayıda döngü yapmak için kullanabilirsiniz
"""

x = range(0,6)
print(x)


"""
Dictionary Kullanımı:
belirli kod blokları arasında belirtilen sayıda döngü yapmak için kullanabilirsiniz
"""
x = {
    "Furkan" : "12354",
    "Firdevs" : "46521",
    "Fırat": "654654"
}

print(x)


"""
Set Kullanımı:
benzersiz öğelerin sıralanmamış bir koleksiyonu olan bir küme oluşturmak için kullanılır.
"""


x = {"Apple", "Banana", "Orange"}
print(x)


"""
Frozenset Kullanımı:
değiştirilemez ve sıralanmamış bir veri türüdür
"""
x = ({"Apple", "Banana", "Orange"})
print(x)

"""
Bool Kullanımı
"""
x = True
print(x)

"""
Bytes Kullanımı:
"""
x = b"Merhaba"
print(x)

"""
Bytearray Kullanımı:
"""
x = bytearray(5)
print(x)

"""
Memoryview Kullanımı:
"""

x = memoryview(bytes(5))
print(x)
