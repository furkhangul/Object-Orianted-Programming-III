"""
Tablodan kayıt seçerken WHERE komutunu kullanabiliriz.
"""
import mysql.connector
adresbul = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)
adresbul_komut = adresbul.cursor()
sql = "SELECT * FROM customers WHERE adress = 'Siirt' "
adresbul_komut.execute(sql)
sonuc = adresbul_komut.fetchall()
for x in sonuc:
    print(x)

"""
Mesela yol geçen kayıtları bulmak için ise %yol% şeklinde arama yapmamız gerekmektedir.
"""
ozelarama = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)
ozelarama_komut = ozelarama.cursor()
sql = "SELECT * FROM customer WHERE adress LIKE %yol%"
ozelarama_komut(sql)
sonuc = ozelarama_komut.fetchall()

for i in sonuc:
    print(i)
    
"""
Şeklinde yazıldığı zaman ise bütün yol geçen yerleri bize döngü ile sunmaktadır.
"""
