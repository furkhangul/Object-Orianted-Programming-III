"""
Tabloyu güncellemek için UPDATE ifadesi kullanılır mesela Siirt ifadesini İstanbul olarak değiştirmek istersek:
"""
import mysql.connector

guncelle = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)
komut1 = guncelle.cursor()
sql = "UPDATE customers SET adress = 'İstanbul' Where adress = 'Siirt' "
komut1.execute(sql)
guncelle.commit()
print(komut1.rowcount, "güncellendi")

"""
commit ifadesi kullanılması şart !
"""


"""
sql injeciton önlemek için placeholderlar aracılığı ile bu işlemi gerçekleştirecek olursak ise:
"""

guncelle = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)
komut1 = guncelle.cursor()
sql = "UPDATE customers SET adress = %s Where adress = %s "
val = ("Siirt","İstanbul")
komut1.execute(sql,val)
guncelle.commit()
print(komut1.rowcount, "güncellendi")
