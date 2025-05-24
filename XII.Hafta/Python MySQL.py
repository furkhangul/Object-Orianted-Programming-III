"""
Python'u veri tabanı sistemlerinde kullanmak mümkündür.
Dünyaca popüler olan MySQL veri tabanı sistemlerini kullanarak göreceğiz.
Bunun için belli kütüphanelere ihtiyacımız var bunların başında ise:
mysql-connector adındaki kütüphaneye ihtiyacımız var.

indirmek için pip install mysql.connector şeklinde terminale yazmamız gerekmektedir.
"""
import mysql.connector


"""
Veritabanını bağlamak için:
"""

data = mysql.connector.connect(
    host = "sql306.epizy.com",
    user = "epiz_34138233",
    password = "oAuoIJHXHf"
)
print(data)


"""
Veritabanı oluşturmak için ise:
NOT: cursor methodu -> connecet ile veritabanına bağlantı sağladık fakat bu veritabanında komut çalıştırmamız için yeterli değil bunun için
cursor yani imleç methodunu kullanmaktayız.
NOT2 : execute methodu -> execute ile ise komutları veri tabanına gönderme işlemini gerçekleştirmekteyiz.
cursor ile "CREATE DATABASE" ile yeni database açabiliriz.
"""

dataolustur = mysql.connector.connect(
    host = "host_adi",
    user = "kullanici_adi",
    password = "password"
)

datakomutgonder  = dataolustur.cursor()

datakomutgonder.execute("CREATE DATABASE datam")


"""
Data olup olmadığını kontrol etmek için ise: 

for döngüsü ile her bir satırı i ile alıp teker teker yazdırmaktayız.
Sisteminizin veritabanlarının bir listesini döndürmekteyiz.
"""

datakontrol = mysql.connector.connect(
    host = "host_name",
    user = "user_name",
    password = "password"
)
datakontrolkomutgonder = datakontrol.cursor()
datakontrolkomutgonder.execute("SHOW DATABASES")

for i in datakontrolkomutgonder:
    print(i)

"""
Sunucuya bağlandığımız zaman database aramak yerine doğrudan database bağlantısı oluşturabiliriz.
Bunun için:

connect kısmına database ekledik ve buradan doğrudan istediğimiz var olan bir databaseye giriş yaptık.
"""

dogrudandatabasebaglan = mysql.connector.connect(
    host = "host_name",
    user = "user_name",
    password = "password",
    database = "database"
)


