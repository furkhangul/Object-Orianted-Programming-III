#Belge, Koleksiyon Silme ve Güncelleme İşlemleri

#Mongo'da belge silme işlemleri:
"""
MongoDB'de bir koleksiyondan belge (kayıt) silmek için delete_one() veya delete_many() metodları kullanılır.
"""
from tkinter.constants import SOLID

#Bir belgeyi silmek için delete_one() fonksiyonu kullanılır.

import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["Database"]
col = db["Customers"]

sorgu = {"adress":"Siirt"}

col.delete_one(sorgu)

#Uyarı: Aynı adrese sahip birden fazla belge varsa sadece ilki silinir.

#Birden fazla belge silme işlemi için delete_many() fonksiyonu kullanılmaktadır.
sorgu = {"adress": {"$regex":"^S"}}
sonuc = col.delete_many(sorgu)
print(sonuc.deleted_count,"Belgesi silindi.")

#Tüm belgeleri silmek için:

none = col.delete_many({})
print(none.deleted_count,"Belge tamamen silindi !")


#Koleksiyon Silme İşlemleri

"""
Bir koleksiyonu yani tabloyu silebilmek için drop() fonkisyonu kullanılmaktadır. col.drop() şeklinde kullanılır.
Eğer koleksiyon varsa silinir. Yoksa sessizce geçer.

"""

col.drop()

#Güncelleme İşlemleri

"""
Tek bir belgeyi güncellemek için update_one() fonkisyonu kullanılmaktadır.
"""
sorgu = {"adress": "Valle 352"}
yeni = {"$set": {"adress":"Siirt"}}

col.update_one(sorgu,yeni)

for belge in col.find():
    print(belge)

"""
Birden fazla belgeyi güncellemek için update_many() fonksiyonu kullanılır.
"""

sorgu = {"adress": {"$ragex":"^S"}}
yeni = {"$set":{"name": "Siirt"}}

sonuc = col.update_many(sorgu,yeni)

print(sonuc.modified_count,"Belge güncellendi !")


#Kayıt sayısını sınırlamak için limit() fonksiyonu kullanılır.

#İlk 5 belgeyi göstermek için:
sonuc = col.find().limit(5)
for belge in sonuc:
    print(belge)
#SQL karşılığı: SELECT * FROM customers LIMIT 5


"""
| Amaç                 | Kod                                              |
| -------------------- | ------------------------------------------------ |
| Tek belge sil        | `delete_one({ "address": "Mountain 21" })`       |
| Çoklu belge sil      | `delete_many({ "address": { "$regex": "^S" } })` |
| Tüm belgeleri sil    | `delete_many({})`                                |
| Koleksiyonu sil      | `drop()`                                         |
| Tek belge güncelle   | `update_one(sorgu, { "$set": {...} })`           |
| Çoklu belge güncelle | `update_many(sorgu, { "$set": {...} })`          |
| Sonuçları sınırla    | `find().limit(5)`                                |

"""
