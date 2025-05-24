"""
Sonucu artan veya azalan düzende sıralamak için ORDER BY ifadesini kullanın.
"""

import mysql.connector
sirala = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)
sirala_komut = sirala.cursor()
sql = "SELECT * FROM customers ORDER BY name"
sirala_komut.execute(sql)
sonuc = sirala_komut.fetchall()
for i in sonuc:
    print(i)

"""
Sonucu artandan azalana çevirmek için DESC kullanılır.
"""

terssirala = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)
terssirala_komut = terssirala.cursor()
sql = "SELECT * FROM customers ORDER BY name DESC"
terssirala_komut.execute(sql)
sonuc = terssirala_komut.fetchall()
for i in sonuc:
    print(i)
