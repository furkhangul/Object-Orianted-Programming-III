#İstatistiksel Önem Testi
"""
İstatistiksel önem testi, bir sonucun rastgele mi yoksa anlamlı mı olduğunu belirlemek için kullanılır.
Örnek:
"Bir öğrencinin sınav sonucu, gerçekten daha mı iyi yoksa sadece tesadüf mü?"
"""

#Temel Kavramlar
"""
| Terim                          | Açıklama                                            |
| ------------------------------ | --------------------------------------------------- |
|    **Hipotez**                 | Nüfus (popülasyon) hakkında bir varsayım.           |
|    **Null (Boş) Hipotez (H₀)** | Fark yok, her şey tesadüf der.                      |
|    *Alternatif Hipotez (H₁)**  | Fark vardır, tesadüf değil der.                     |
|    **Tek Kuyruklu Test**       | Sadece bir yönde fark arar (örn: daha büyük).       |
|   ️  **İki Kuyruklu Test**       | Her iki yönde de fark arar.                         |
|    **Alfa (α)**                | Anlamlılık eşiği (genelde 0.05).                    |
|    **P-Değeri**                | Verinin uçluk derecesi. Küçükse → anlamlı olabilir. |

"""
#Eğer p-değeri <= alfa, boş hipotez reddedilir. Yoksa kabul edilir.

#T-Testi
#İki grup arasında ortalama farkı var mı?
import numpy as np
from scipy.stats import ttest_ind

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

res = ttest_ind(v1, v2)
print(res)

#KS-Testi
"""
Bir dizinin belirli bir dağılıma (örn: normal) uyup uymadığını kontrol eder.
"""
from scipy.stats import kstest

v = np.random.normal(size=100)
res = kstest(v, 'norm')
print(res)

# Betimleyici İstatistikler
"""
Bir dizideki istatistiksel bilgilerin özetini verir.
"""
from scipy.stats import describe

v = np.random.normal(size=100)
res = describe(v)
print(res)

#Normallik Testi

#Eğrilik ve Basıklık
from scipy.stats import skew, kurtosis

v = np.random.normal(size=100)
print(skew(v))       # ~0 olmalı
print(kurtosis(v))   # ~0 olmalı

#normaltest()
#Verilerin normal dağılıma uyup uymadığını test eder.
from scipy.stats import normaltest

v = np.random.normal(size=100)
print(normaltest(v))


#Tablo
"""
| Fonksiyon               | Amaç                             | Sonuç Tipi           |
| ----------------------- | -------------------------------- | -------------------- |
| `ttest_ind()`           | İki grubun ortalaması farklı mı? | T değeri, p-değeri   |
| `kstest()`              | Veri belirli dağılıma uyuyor mu? | KS değeri, p-değeri  |
| `describe()`            | Verinin temel istatistik özeti   | Ortalama, varyans... |
| `skew()` / `kurtosis()` | Eğrilik & basıklık analizi       | Sayısal değerler     |
| `normaltest()`          | Veri normal mi?                  | p-değeri ile sonuç   |

"""


"""
İstatistiksel testlerin yorumlanmasında sık kullanılan bir eşik:

p < 0.05 → anlamlı sonuç, H₀ reddedilir

p ≥ 0.05 → anlamlı değil, H₀ kabul edilir
"""
