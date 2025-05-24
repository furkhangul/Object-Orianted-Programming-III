"""
Pandas verileri analiz etmek için kullanılır.
indirmek için 'pip install pandas' kodunu terminalde çalıştırmamız gerekmektedir. Bazı IDE lerde otomatik olarak zaten mevcuttur.
projeye dahil etmek için ise :
"""
import pandas as pd

#pandas as pd ifadesi pandas kütüphanesini pd olarak kısaltamaya yarar.

#Pandas verileri kümelemeye yarıyan bir kütüphanedir. Verileri analiz etme, temizleme ve işleme işlevlerine sahiptir.

#Pandasta kütüphanenin sürümünü kontrol etmek için:
print(pd.__version__)
print()

#Pandas serileri verileri sütun şeklinde tek sıra halinde tutan dizidir.
a = [1,2,3,4]
seri =pd.Series(a)
print(seri)
print()

#Değerleri istediğimiz indexe göre çağırmak istersek:
print(f"Seçilen Değer {seri[0]}")

#Pandasta normalde değerler 0 1 2 3 şeklinde devam eder fakat biz bunları değiştirebiliriz.
print()
degismis_seri = pd.Series(a,index=["x","y","z","q"])
print(degismis_seri)
print()

#Ekisik girilirse hata mesajı alınır yani girdi kadar index belirlememiz gerekmektedir.

#Bunları da çağırmak için
print(f"Çağırlmış yeni indeksli sayı: {degismis_seri["z"]}")
print()



#Bunlara gerek kalmadan direkt key value değerleri ile kendimiz doğrudan ekleme yapabiliriz.
key_value = {"Furkan":21, "Ferhat":20, "Yusuf":19, "Kerem":22}
key_value_seri = pd.Series(key_value)
print(key_value_seri)
print()



#Çağırmak için de artık keyler kullanılır.
print(f"Key ile çağırıldı: {key_value_seri["Furkan"]}")

print()
#Yalnızca belirli kodları almak için ise aynı dizide keyleri seçmemiz gerekmektedir.
ozelsecim = pd.Series(key_value, index= ["Furkan", "Yusuf"])
print(ozelsecim)
