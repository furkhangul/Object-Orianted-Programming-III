"""
Setler: {} aralığı içerinde ifade edilir.
Listeler: [] aralığında ifade edilir.
Tuplelar: () aralığında ifade edilir.
Dictionaryler: {,} şeklinde ifade edilir.
"""


"""
Bir set örenği verecek olursak:
"""
thisset = {"apple", "banana", "cherry"}
print(thisset)


"""Bir set farklı veri yapıları içerebilir."""
set1 = {"abc", 34, True, 40, "male"}
print(set1)

"""Bir setin tipi:"""
print(type(set1))

"""SET() kurucu yapısı"""
thisset = set(("apple", "banana", "cherry")) #İki parantez olmasına dikkat!
print(thisset)

"""Bir değerin varlığını sorgulama"""
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

"""Ekleme işlemi add() ile yapılır."""
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

"""
Uninon() metodu ile iki seti birleştirme.
"""
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

"""
Update metodu ile iki seti birleştirme.
"""
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)


"""
Dictionary Modeli: 
"""

kitaplik = {
    "isim" : "Furkan",
    "soyisim" : "Gül",
    "yas" : 21,
    "boy" : 175,
    "kilo" : 72,
    "Durum" : "Bekar"
 }
print(kitaplik)


"""
İç içe de yazabiliriz:
"""

data  = {
    "_furkan.gul": {
        "isim" : "Furkan",
        "soyisim" : "Gül",
        "Yaş" : 21
    }
}

print(data)

"""
keys ile anahtarları listele
"""
datakeyler = data.keys()
print(datakeyler)



