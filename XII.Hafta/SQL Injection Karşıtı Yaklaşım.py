"""
SQL INJECTION önlemek için placeholderlar kullanılır.
Burada doğrudan almaz dolaylı yoldan yani %s formatı ile adr üzerinden bilgiyi alır.
"""
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Siirt", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
 print(x)

 """
 Eğer bu şekilde kullanmasaydık 
 
 SELECT * FROM users WHERE username = 'admin' OR 1=1
 
 şeklinde yazmış olsaydık adminin yetkileri ile her şeyi doğru olarak işaretleyebilirdik.
 """

 
 """
 Verileri SQL Injectiondan sakınarak silmek için ise:
 """

 sil = mysql.connector.connect(
     host="localhost",
     user="yourusername",
     password="yourpassword",
     database="mydatabase"
 )
 sil_komut = mydb.cursor()
 sql = "DELETE FROM customers WHERE address = %s"
 adr = ("Yellow Garden 2",)
 sil_komut.execute(sql, adr)
 sil.commit()
 print(sil_komut.rowcount, "record(s) deleted")
