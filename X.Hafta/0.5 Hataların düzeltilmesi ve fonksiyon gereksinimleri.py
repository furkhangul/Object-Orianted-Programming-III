"""
Bazen nan değeri yeirne format hatası olabilmektedir. Örneğin tarih kısmına 11202004 şeklinde / koymadan yazıldığı zaman bunu düzeltebiliriz.
"""
import pandas as pd
df = pd.read_csv('dirtydata.csv')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
print(df.to_string)

"""
Eğer tarih hatalı değil ise ve gözükmüyorsa direkt tarihi silmekte fayda vardır.
"""
data1 = pd.read_csv("dirtydata.csv")
data1.dropna(subset = ["Date"],inplace=True)
print(data1)


"""
Bazen değerleri silmek yerine değiştirmemiz gerekmektedir. Bunun için
"""

#Bu kodda 7. satıda süre kısmını 45 ile değiştirdik.
data = pd.read_csv("dirtydata.csv")
data.loc[7, "Duration"] = 45


#Başka bir sınama ifadesi kullanmak isteseydik

if data.loc[7, "Duration"] > 120:
    data.loc[7 , "Duration"] = 120



"""
Komple satırı silmek istediğimizde ise drop() fonksiyonu devreye girer
"""
if data.loc[12, "Duration"] > 120:
    data.drop(12, inplace = True)


"""
Veriler birden fazla defa kendini tekrar etmiş ise bu verileri duplicated fonksiyonu ile bulabiliriz.
"""

print(data.duplicated())

#Yinelenen her satırı silmek için ise
data.drop_duplicates(inplace=True)
print(data)
