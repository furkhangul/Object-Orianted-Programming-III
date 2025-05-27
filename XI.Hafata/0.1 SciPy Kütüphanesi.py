#SciPy Kütüphanesi
"""
Scipy kütüphanesi, bilimsel ve teknik hesaplamalar için geliştirilmiş güçlü bir Python kütüphanesidir. Temelinde Numpy bulunur yani
Scipy çalıştırılabilmesi için Numpy kütüphanesine ihtiyaç duyar.

SciPy, adını (Scientific Python) açılımından almaktadır.

Kütüphane:
Optimizasyon
İstatistiksel Hesaplamalar
Sinyal İşleme
Lineer Cebir
Fourier dönüşümleri ve daha fazlası için kullanınlmaktadır.

NumPy'de olmayan ekstra bilimsel fonksiyonlar içerir.

Daha gelişmiş matematiksel işlemler sunar.

Performans açısından optimize edilmiş çözümler sağlar.

Scipy bazı performans odaklı bölümleri ise C dilinde yazılmıştır (daha hızlı çalışması için).

Scipy indirebilmek için klasik olan pip modülü ile terminale:
pip install scipy
yazmamız yeterlidir.
"""

#Kodumuza import etmek için
import scipy

#Scipy kütüphanesinin versiyonunu kontrol etmek için ise:

print(scipy.__version__)
