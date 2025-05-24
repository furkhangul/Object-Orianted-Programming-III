"""
Pandastaki veri kümeleri genellikle DataFrame adı verilen çok boyutlu tablolardır.
Seri bir sütun gibidir. DataFrame tablodur.
"""

#İmport edecek olursak
import pandas as pd
#Şimdir örnek bir dataframe oluşturacak olursak.
data = {
    "username": ["_furkan.gul", "fatih.terim", "selim__can"],
    "password": ["furkangul", "fatiterim123", "selimcan123selim"]
}
framedata = pd.DataFrame(data)
print(framedata)

#Belirli bir satırı almak ister isek loc() fonkisyonunu kullanmamız gerekmektedir.
print()
print(f"Seçilen kullanıcı bilgileri:\n{framedata.loc[0]}")

#Birden fazla çağırmak için:
#Ekstra bir köşeli parantez kullanıldı.
print()
print(f"Seçilen kullanıcılar :\n{framedata.loc[[0,1]]}")


#DataFrameleri de seriler gibi indekslerini değiştirebiliriz.
print()
degismis_dataframe = pd.DataFrame(data, index = ["user1", "user2", "user3"])
print(degismis_dataframe)

#Çağırmak için ise:
#Serilerden farklı olarak .loc() ifadesi kullanılmaktadır.
print(f'\n Çağırılan Özel DataFrame: {degismis_dataframe.loc["user1"]}')



#Dışarıdan csv verileri alarak bu işlemleri gerçekleştirecek olursak:
csv_verileri = pd.read_csv("ornek.csv")
print(csv_verileri)
print()

#DataFramenin tamamını yazdırmak için to_string() fonksiyonu çalıştırılması gerekmektedir.
tamaminioku  = csv_verileri.to_string()
print(tamaminioku)
print()

#Bazen çok büyük satırlı ve sütunlu veriler gelirse terminalimiz dolabilir bunun için farklı yöntemler mevcut
# pd.options.display.max_rows adlı ifade ile display olarak 60 satır üzerindeki ifadelerde otomatik olarak ilk 5
# ve son 5 satırı gösterir

#kendimiz ifadenin default ayarları ile oynayarak arttırıp azaltabiliriz.
pd.options.display.max_rows = 15
oku = pd.read_csv("ornek.csv")
print(oku)

