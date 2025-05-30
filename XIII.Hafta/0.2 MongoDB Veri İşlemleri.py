#Veritabanı oluşturma
"""
MongoDB de veri tabanı oluşturmak için önce MongoClient sınıfı ile MongoDB sunucusuna bağlanılır.
Ancak MongoDB'den veritabanı hemen oluşturulamaz. İçine bir koleksiyon veya en az bir belge eklenene kadar sadece ad olarak sunucu var olur.
"""
import pymongo
# MongoDB sunucusuna bağlan (localhost:27017 varsayılan adrestir)

sunucu = pymongo.MongoClient("mongodb://localhost:27017")

# "database" adında bir veritabanı nesnesi oluşturulur.
nesne = sunucu["Database"]


#Veritabanının var olup olmadığını kontrol etmek için:
#Not: Veritabanı içine veri eklenene kadar MongoDB veritabanını oluşturmaz.

arama = sunucu.list_collection_names()
if "Database" in arama:
    print("Database adında bir veritabanı mevcuttur.")
else:
    print("Veritabanı daha oluşturulmamıştır.")


#Koleksiyon Oluşturma

"""
MongoDB'de koleksiyon SQL'deki tabloların karşılığıdır.
Bir veritabanı içerisinde bir veya birden fazla koleksiyon bulunabilir. Ancak tıpkı veritabanında olduğu gibi, MongoDB bir belge 
eklenene kadar koleksiyonu fiziksel olarak oluşturamaz.
"""

koleksiyon = pymongo.MongoClient()
# "Müşteriler" adlı bir koleksiyon oluşturuluyor
yenikoleksiyon = koleksiyon["Database"]
yeni = yenikoleksiyon["Müşteriler"]


#KOLEKSİYON KONTROLÜ
koleksiyonarama = yenikoleksiyon.list_database_names()
if "Müşteriler" in koleksiyonarama:
    print("Müşteriler adında bir koleksiyon mevcuttur.")
else:
    print("Veritabanı mevcut değildir. ")


#Belge ekleme işlemleri

"""
Bir koleksiyona yeni bir kayıt yani belge eklemek için insert_one() fonksiyonu kullanılmaktadır. Her belge bir Python dict nesnesi olarak tanınır.
"""

dosya = pymongo.MongoClient("mongodb://localhost:27017")
ilk = dosya["Database"]
iki = ilk["Customers"]

listem = {"furkan":"the.lord","şevket":"Sevko.132","ramiz":"kralramiz"}

#Belge ekle:
ekle = iki.insert_one(listem)

print("Eklenen belgenin id'si:",ekle.inserted_id)


#Birden fazla veri ekleme işlemi:

ozel = pymongo.MongoClient("mongodb://localhost:27017")
data = ozel["Database"]
coll = data["Info"]
mylist = [
    {"name": "Amy", "address": "Apple st 652"},
    {"name": "Hannah", "address": "Mountain 21"},
    {"name": "Michael", "address": "Valley 345"},
    {"name": "Sandy", "address": "Ocean blvd 2"},
    {"name": "Betty", "address": "Green Grass 1"},
    {"name": "Richard", "address": "Sky st 331"},
    {"name": "Susan", "address": "One way 98"},
    {"name": "Vicky", "address": "Yellow Garden 2"},
    {"name": "Ben", "address": "Park Lane 38"},
    {"name": "William", "address": "Central st 954"},
    {"name": "Chuck", "address": "Main Road 989"},
    {"name": "Viola", "address": "Sideway 1633"}
]
ekle1 = coll.insert_many(mylist)
print("Eklenen belgelerin _id değerleri:", ekle1.inserted_ids)
#Birden fazla veri eklemek için: insert_many() fonksiyonu kullanılmaktadır.


#Belli bir id değerleri ile veri ekleme
#MongoDB her belgeye otomatik olarak bir _id atar. Ancak isterseniz bu değeri manuel olarak da belirleyebilirsiniz. Dikkat! _id değerleri benzersiz olmalıdır.

special = pymongo.MongoClient("mongodb://localhost:27017")
data1 = special["Database"]
coll1 = data1["Customers"]

mylist2 = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x1 = coll1.insert_many(mylist2)
print("Eklenen dosyların _id değerleri:", x1.inserted_ids)


"""
| Aşama                | Açıklama                            |
| -------------------- | ----------------------------------- |
| Veritabanı Oluşturma | `myclient["veritabani_adi"]`        |
| Koleksiyon Oluşturma | `mydb["koleksiyon_adi"]`            |
| Tek Belge Ekleme     | `insert_one({...})`                 |
| Çoklu Belge Ekleme   | `insert_many([{...}, {...}])`       |
| Özel \_id ile Ekleme | Her belgeye `_id` alanı eklenebilir |

"""

"""
Ekstra:
Verileri sorgulama (find, find_one)

Filtreleme ve koşullar

Sıralama

Güncelleme (update_one, update_many)

Silme (delete_one, delete_many)
"""
