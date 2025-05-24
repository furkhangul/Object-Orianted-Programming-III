"""
MySQL database tablo eklemek için:
"""
import mysql.connector

tablosql = mysql.connector.connect(
    host ="host",
    user = "username",
    password = "password",
    database = "database"
)

tabloimlec = tablosql.cursor()
sql = "INSERT INTO customer (name, adress) VALUES (%s, %s)"
val = ("Furkan ", "Siirt-Merkez")
tabloimlec.execute(sql,val)
tablosql.commit()
print(tabloimlec.rowcount, "satır eklendi.")
"""
Bu kodda 
sql yazısı içerisinde: 
    INSERT INTO : içeriye aktar
    customer: müşteri tablosuna veri eklenecek
    (name,adress): isim ve adress bölümlerine
    VALUES( %s, %s ): val değerlerinde girilen girdileri sırası ile eklemek için kullanıldı.
"""
"""
commit methodu Yapılan değişiklik (INSERT işlemi) kalıcı hale getirilir. kessinlikle kullanılması gerekmektedir aksi takdirde kod kendi kendini kayıt edemez bu method 
ile tablo kayıt edilir ve çağırıldığı zaman yeni tabloyu önümüze çıkarır.
"""

"""
print(tabloimlec.rowcount, "satır eklendi.") kodu ise ekraran bir satır eklendiğini söyler bize.
"""


"""
Birden fazla satır eklemek için:
"""

bircok = mysql.connector.connect(
    host = "host",
    user = "username",
    password = "password",
    database = "database"
)
bircokkomut = bircok.cursor()
sql = "INSERT INTO customer (name, adress) VALUE (%s, %s)"
var = [
    ("Furkan" ,"Siirt"),
    ("Fırat", "Van"),
    ("Umut", "Diyarbakır")
]

bircokkomut.execute(sql,val)
bircok.commit()

print(bircokkomut.rowcount, "satır eklendi")


"""
Eklenen kimliği yazdırmak için:
"""

eklenenioku = mysql.connector.connect(
    host = "host",
    user = "username",
    password = "password",
    database = "database"
)
ekleneniokukomut = eklenenioku.curser()
sql = "INSERT INTO customer (name, adress) VALUE (%s, %s)"
val = ("Furkan", "Siirt")
ekleneniokukomut.execute(sql,val)
eklenenioku.commit()
print("son eklenen: ", ekleneniokukomut.lastrowid)


"""
Tüm müşteri kayıtlarını göstermek istersek:

SELECT * FROM customer komutu ile müşterileri seçtiğimizi göstermekteyiz.

fetchall komutu ile ise son yürütülen ifadenin satırlarını getirir yani yukarıdaki customeri yürüttüğü için customerin satırlarını getirecek.
"""

tummusteri = mysql.connector.connect(
host="localhost",
user="yourusername",
password="yourpassword",
database="mydatabase"
)

tummusteri_komut = tummusteri.cursor()
tummusteri_komut.execute("SELECT * FROM customers")
sonuc = tummusteri_komut.fetchall()

for i in sonuc:
    print(i)

"""
Özel olarak sütunları seçecek olursak:
"""

ozelsec = mysql.connector.connect(
host="localhost",
user="yourusername",
password="yourpassword",
database="mydatabase"
)

ozelsec_komut = tummusteri.cursor()
ozelsec_komut.execute("SELECT name, adress FROM customers")
sonuc = tummusteri_komut.fetchall()

for i in sonuc:
    print(i)

"""
Yalnızca satırlar ile ilgileniyorsal 
fatchone komutunu kullanmaktayız. Bu komut ile istediğimiz satırın indexini girersek o satırı bize vermekte
default olarak fatchone() ifadesi ise ilk komutu bize vermektedir.
"""

satir = mysql.connector.connect(
    host = "host",
    user = "user",
    password = "password",
    database = "database"
)

satir_komut = satir.cursor()
satir_komut.execute("SELECT * FORM customer")
sonuc = satir_komut.fetchone()

print(sonuc)
