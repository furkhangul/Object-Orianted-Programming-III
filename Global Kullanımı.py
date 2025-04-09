#Global anahtar sözcüğünü kullanırsanız, değişken global kapsama aittir:

def deger():
    global y
    y  = "rasim"
deger()
#Bir fonksiyon içindeki global değişkenin değerini değiştirmek için global anahtar kelimeyi
#kullanarak değişkene bakın:
x = "nesne"

def kullan():
    global x
    x="hello"
    print(x)
kullan()
