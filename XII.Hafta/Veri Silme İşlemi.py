"""
Tablodan veri silmek için:
"""
import mysql.connector

sil = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)
komut1 = sil.cursor()
sql = "DELETE FROM customers WHERE address = 'Siirt'"
komut1.execute(sql)
sil.commit()
print(komut1.rowcount, "kayıt silindi.")


"""
Tablo Silmek için ise:
DROP TABLE ifadesi kullanılmaktadır.
"""

tablosil = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)
komut2 = tablosil.cursor()
sql = "DROP TABLE customers"
komut2.execute(sql)


"""
Bazı durumlarda aradığımız tabloyu bulamayabiliriz bundan dolayı sıkıntılar da yaşayabiliriz. 
Bunun için tabloyu silmeden yapmamız gereken şey tablonun var olup oladığını kontrol ettikten sonra silmek.
İF EXİST ifadesi ile bu kontrol sağlanır ve silinmesi gereken tablo eğer mevcut ise silinmektedir.
"""

kontrolilesil = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)
komut3 = kontrolilesil.cursor()
sql = "DROP TABLE IF EXİST customers"
komut2.execute(sql)
