#MongoDB'de Arama ve Filtreleme İşlemleri

#Mongo'da veri bulma:
"""
Mongo'da veri aramak için, SQL'deki SELECT komutu benzerdir. Python'da MongoDB ile veri bulmak için find() ve find_one() fonksiyonları kullanılır.
"""
import pymongo

#Tek belgeyi bulmak için: find_one()

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["Database"]
coll = db["Customers"]

sonuc = coll.find_one()
print(sonuc)

#Eğer koleksiyonda hiç belge yoksa None döner.


#Tüm belgeleri bulmak için: find()
"""
Koleksiyondaki tüm belgeleri getirir. SQL’deki SELECT * FROM tablo işlemi gibidir.
"""

for belge in coll.find():
    print(belge)

#Bu işlem her belgeyi dict (sözlük) biçiminde getirir.

#Özel arama için:
for belge in coll.find({}, {"_id":0, "name":1,"adress":0}):
    print(belge)


#Sadece address hariç tüm alanlar:
for belge in coll.find({},{"adress":0}):
    print(belge)

#Aynı anda hem 1 hem 0 kullanılamaz, yalnızca _id istisnadır.

#Belirli bir şarta göre arama yapmamız için:

sorgu = {"name": "Furkan"}
for belge in coll.find(sorgu):
    print(belge)

#Karşılaştırma Operatörleri ile Sorgu
#MongoDB’de sorgulara karşılaştırıcılar da eklenebilir (SQL'deki >, <, >=, != gibi).

#Adress değerinin S den büyük olanları seçmek için $gt : "S" kullanırız.

sorgu = {"adress":{"$gt": "S"}}
for belge in coll.find(sorgu):
    print(belge)

"""
| Operatör | Açıklama       |
| -------- | -------------- |
| `$gt`    | Büyüktür       |
| `$lt`    | Küçüktür       |
| `$gte`   | Büyük eşit     |
| `$lte`   | Küçük eşit     |
| `$ne`    | Eşit değil     |
| `$eq`    | Eşittir        |
| `$in`    | İçinde olan    |
| `$nin`   | İçinde olmayan |

"""

#Regex işlemleri
#MongoDB’de regex kullanarak string eşleşmeleri yapılabilir.

# "address" alanı "S" harfi ile başlayanlar (^S):

sorgu = {"adress": {"$regex": "^S"}}

for belge in coll.find(sorgu):
    print(belge)
#Regex yalnızca metin alanlarında kullanılabilir.

"""
| İşlem                  | Metot                   | Açıklama                  |
| ---------------------- | ----------------------- | ------------------------- |
| Tek belge getir        | `find_one()`            | İlk belgeyi getirir       |
| Tüm belgeleri getir    | `find()`                | Tüm belgeleri getirir     |
| Alanları seçerek getir | `find({}, {…})`         | Belirli alanları seçme    |
| Şartlı sorgu           | `find({"alan": deger})` | Şartla filtreleme         |
| Karşılaştırmalı sorgu  | `{"alan": {"$gt": …}}`  | Büyük/küçük gibi sorgular |
| Regex ile arama        | `{"alan": {"$regex"}}`  | Metin eşleşmeleri için    |

"""
