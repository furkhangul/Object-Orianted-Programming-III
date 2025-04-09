"""
Python'da 4 farklı koleksiyon tipi vardır.
1. Liste
2. Tuple
3. Set
4. Dictionary

Listeler, birden çok öğeyi tek bir değişkende saklamak için kullanılır
"""


liste = ["Merhaba", "Benim","Adım", "Furkan"]
print(liste)


"""
Lise uzunluğunu len formatı ile bulabiliriz:
"""

print(len(liste))


"""
Liste farklı türlerde olabilir.
"""

liste2 = [1 , True, "Merhaba", 165, 0.5]

print(liste2)


"""
Type kullanımı ile hangi veri tipi olduğunu öğrenebiliyorduk.
"""

print(type(liste2))


"""
Liste yapmak için list() kurucusu kullanımı.
"""

listeyap = list(("Hello", "Ben" , "Furkan"))


"""
Elemanlara erişim:
"""

meyveler = ["Elma", "Armut", "Kiraz", "Karpuz", "Vişne"]
print(meyveler[1])
print(meyveler[-1])
print(meyveler[1:3])
"""
1 den 3 e kadar olan yerler
"""


"""
Listeyi genişletme
"""
buListe = ["elma", "muz", "kiraz"]
tropikal = ["mango", "ananas", "papaya"]
buListe.extend(tropikal)
print(buListe)


"""
Remove silme işlemi gerçekleştirebiliriz.
"""

buListe = ["elma", "muz", "kiraz"]
buListe.remove("muz") # Muz silinir.
print(buListe)


"""
Pop ile en son eklenen veriyi silebiliriz.
"""

buListe = ["elma", "muz", "kiraz"]
buListe.pop()  # Kiraz silinir en son eklendiği için
buListe.pop(1) # Sondan eklenen ikinci nesneyi siler
print(buListe)

"""
del anahtar sözcüğü ayrıca listeyi tamamen silebilir.
"""
buListe = ["elma", "muz", "kiraz"]
del buListe[0]
print(buListe)

buListe = ["elma", "muz", "kiraz"]
del buListe


"""
Sort ile listeyi alfabetik bir şekilde sıralayaibliyoruz.
"""

buListe = ["portakal", "mango", "kivi", "ananas", "muz"]
buListe.sort()
print(buListe)


"""
Reserve ile listeyi tersine çevirebiliriz.
"""

buListe = ["muz", "Portakal", "Kivi", "kiraz"]
buListe.reverse()
print(buListe)


"""
Listeleri teker teker eklemek için 
"""

liste1 = ["a", "b" , "c"]
liste3 = [1, 2, 3]
for x in liste3:
    liste1.append(x)
print(liste1)

"""
list1'in sonuna list2 eklemek için extension() yöntemini kullanın
"""
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)



"""

append() Listenin sonuna bir öğe ekler
clear() Tüm öğeleri listeden kaldırır
copy() Listenin bir kopyasını döndürür
count() Belirtilen değere sahip öğelerin sayısını döndürür
extend() Geçerli listenin sonuna bir listenin öğelerini (veya herhangi bir yinelenebilir) ekleyin
index() Belirtilen değere sahip ilk öğenin dizinini döndürür
insert() Belirtilen konuma bir eleman ekler
pop() Belirtilen konumdaki öğeyi kaldırır
remove() Belirtilen değere sahip öğeyi kaldırır
reverse() Listenin sırasını tersine çevirir
sort() Listeyi sıralar

"""



"""

count() Bir tanımlama grubunda belirtilen bir değerin kaç kez oluştuğunu
döndürür
index() Tuple'ı belirtile

"""
