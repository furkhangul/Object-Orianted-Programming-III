import numpy as np


arabalar = ["BMW", "AUDİ", "TOYOTA"]

print(arabalar[0])
print(len(arabalar))

"""
eklemek için
"""

arabalar.append("VOLVO")
print(arabalar)

"""
En sonuncuyu çıakrmak için
"""

arabalar.pop()
print(arabalar)

"""
Direkt silmek için remove kullanılır
"""

arabalar.remove("BMW")
print(arabalar)


"""
append() Listenin sonuna bir eleman ekler
clear() Listedeki tüm öğeleri kaldırır
copy() Listenin bir kopyasını döndürür
count() Belirtilen değere sahip öğelerin sayısını döndürür
extension() Bir listenin (veya herhangi bir yinelenebilirin) öğelerini geçerli listenin sonuna
ekleyin
index() Belirtilen değere sahip ilk öğenin dizinini döndürür
insert() Belirtilen konuma bir eleman ekler
pop() Belirtilen konumdaki öğeyi kaldırır
remove() Belirtilen değere sahip ilk öğeyi kaldırır
reverse() Listenin sırasını tersine çevirir
sort() Listeyi sıralar
"""

