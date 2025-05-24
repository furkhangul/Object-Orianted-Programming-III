"""
"LIMIT" ifadesini kullanarak sorgudan döndürülen kayıt sayısını sınırlayabilirsiniz
"""
import mysql.connector

limit = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)
komut1 = limit.cursor()
sql = "SELECT * FROM customers LIMIT 5"
komut1.execute(sql)
sonuc = komut1.fetchall()

for i in sonuc:
    print(i)


"""
Başka bir konumdan başlayarak seçme işlemi gerçekleştirmek için OFSET sorgusu uygulanır.
Bu kodda 3. değerden başlayarak 5. değere kadar seçen fonksiyonu ifade etmektedir.
"""

pozisyon = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)
komut2 = pozisyon.cursor()
sql = "SELECT * FROM customer LIMIT 5 OFSET 2"
komut2.execute(sql)
sonuc2 = komut2.fetchall()

for i in sonuc2:
    print(i)








"""
JOİN KULLANIMI:
"""

"""
JOIN, veritabanında birden fazla tabloyu birleştirmek için kullanılır. Genellikle, tablolar arasında ortak sütun 
(örneğin id) bulunur. Bu ortak sütunlar üzerinden eşleştirme yapılır.
"""

"""
users tablosu:
id	name	fav
1	John	154
2	Peter	154
3	Amy	155
4	Hannah	NULL
5	Michael	NULL
"""
"""
products tablosu:
id	name
154	Chocolate Heaven
155	Tasty Lemons
156	Vanilla Dreams
"""

join = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)
join_komutu = join.cursor()

sql = "SELECT users.name  AS user / SELECT products.name AS favorite/ From users / INNER JOİN products ON users.fav = products.id"
join_komutu(sql)
sonuc = join_komutu.fetchall()
for i in sonuc:
    print(i)
"""
INNER JOİN yerine JOİN kullanılabilir.
"""



"""
LEFT JOİN ifadesi ise soldaki boşta kalan isimler tam olarak sağdaki tabloya uygun değilse yani sağdaki tabloda
yeterince ürün yoksa NULL ifadesini döndürür ve listeye ekler 
"""

left = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)
left_komut = left.cursor()
sql = "SELECT users.name AS user / SELECT producers.name AS favorite / FROM users / LEFT JOİN producers ON users.fav = producers.id"
left_komut.execute(sql)
sonuc =left_komut.fetchall()
for i in sonuc:
    print(i)

"""
RIGHT JOIN komutu ise tam tersi olarak sağdaki tamamlanmamış ürünleri soldaki değelere null getirerek listeye ekler. 
"""

right = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)
right_komut = right.cursor()
sql = "SELECT users.name AS user / SELECT producers.name AS favorite / FROM users / LEFT JOİN producers ON users.fav = producers.id"
right_komut.execute(sql)
sonuc = right_komut.fetchall()
for i in sonuc:
    print(i)
