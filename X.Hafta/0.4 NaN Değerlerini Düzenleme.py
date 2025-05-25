import pandas as pd
"""
Boş hücreler veri analizi sırasında belli başlı sorunlara neden olabilmektedir.
Boş hücreler ile başa çıkmanın yolu boş olan satırları silmektir.
Veri kümeleri çok büyüktür bundan dolayı birkaç satırın silinmesi sonucu çok fazla etkilememektedir.
"""
#Kirli yani null barındıran bir data ile yola devam edecek olursak
data = pd.read_csv("dirtydata.csv")
#yeni_data = data.dropna()
#print(yeni_data)

"""
Dropna() fonksiyonu pandasta içeri aktardığımız datada nan olarak geçen satırları es geçerek bize datayı temizleyip sunmaktadır.
Örnekte verdiğimiz üzere 22. satırda nan değeri varken dropna bu satırı çıktı olarak vermeyip doğrudan 21 den 23 e geçerek hataların önlenmesini
sağlamaya çalışmıştır.
"""

#Geçen örnekte ana datamızdan farklı olarak bir data üreterek onun üzerinden silme işlemini gerçekleşitrmiştik.
#Fakat bu örnekte ise doğrudan datadan silinme işemini gerçekleştireceğiz.
#data.dropna(inplace=True)
#print(data)

"""
Boş değerleri silmek yerine alternatiflerimiz de vardır mesela boş olan bir satırı fakrlı değerler ile 
doldurarak veri kaybını önleyebilmekteyiz bunun için de fillna() fonkisyonunu kullanmaktayız.
"""

#data.fillna(130, inplace= True)
#print(data)

#Evet 130 ile çevirdik ama bu bütün null değerleri için geçerliydi mesela artık tarih kısmı da 130 ile değişti ama bunu önlemek için
#özel olarak sütun ve satır belirterek bu işlemi gerçekleşitirebiliyoruz.

#data["Calories"].fillna(130,inplace = True)
#print(data)

#Daha tutarlı sonuçlar almak için 130 gibi kafadan bir sayı değil de ortalama veya medyan ile bu sayıyı üretebiliriz.
#Bu hem ortalamayı çok fazla değiştirmez hem tutarlılığı maksimum seviyeye çıkarır.


#Ortalama için
ortalama = data["Calories"].mean()
data["Calories"].fillna(ortalama,inplace = True)
print(data)

#Medyan için
median = data["Calories"].median()
data["Calories"].fillna(median,inplace = True)
print(data)

#Mod için
mod = data["Calories"].mode()
data["Calories"].fillna(mod,inplace = True)
print(data)
