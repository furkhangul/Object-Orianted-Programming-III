#Pandas Veri Kolorasyonu

#Corr() fonkisyonu sayısal sütunların kendi aralarında ilişkisini ölçmede kullanılır.
#Örnek olarak :
# Bir kişi daha uzun süre spor yaparsa, daha fazla kalori yakar mı?
#Nabız yükseldikçe harcanan enerji artıyor mu?

import pandas as pd

df = pd.read_csv("data.csv")
print(df.corr())

"""

Değerler -1 ile +1 arasında değişir.

+1 → Mükemmel pozitif ilişki (biri artarsa diğeri de artar)

-1 → Mükemmel negatif ilişki (biri artarsa diğeri azalır)

0 → Hiçbir ilişki yok

"""


"""

Duration ve Calories: 0.92 → Çok güçlü pozitif ilişki: uzun süre spor yaparsan daha çok kalori yakarsın.

Duration ve Pulse: -0.15 → Çok zayıf ve negatif bir ilişki: spor süresiyle nabız arasında anlamlı bir bağ yok.

Pulse ve Maxpulse: 0.78 → Oldukça güçlü ilişki: nabız yüksekse, maksimum nabız da yüksek olma eğilimindedir.

Maxpulse ve Calories: 0.20 → Zayıf ilişki: maksimum nabızla kalori yakımı arasında çok anlamlı bir bağ yok.

"""

"""
Korelasyon Değeri	Yorum
0.0 – 0.3	         Zayıf ilişki
0.3 – 0.6	         Orta düzeyde ilişki
0.6 – 0.9	         Güçlü ilişki
0.9 – 1.0	         Çok güçlü ilişki (mükemmel)
"""
