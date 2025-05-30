#MongoDB'de Sıralama İşlemleri

"""
MongoDB'de sorgu sonuçlarını artan (A–Z) veya azalan (Z–A) şekilde sıralamak için sort() metodu kullanılır.

Bu işlem, SQL'deki ORDER BY ifadesine karşılık gelir.
"""

#Sıralama işlemine örnek:

import pymongo

client = pymongo.MongoClient("mongodb://localost:27017")
db = client["Database"]
col = db["Customers"]

sonuclar = col.find().sort("name",1)
for belge in sonuclar:
    print(belge)

#Yapısına bakacak olursak:
"""
collection.find().sort("alan_adı", sıralama_yönü)
| Parametre    | Açıklama                       |
| ------------ | ------------------------------ |
| `"alan_adı"` | Sıralamak istediğiniz alan adı |
| `1`          | Artan sıralama (varsayılan)    |
| `-1`         | Azalan sıralama                |

"""
