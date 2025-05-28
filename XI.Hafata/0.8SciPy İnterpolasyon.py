#SciPy İnterpolasyon
"""
İnterpolasyon, verilen iki nokta arasında yeni ara noktalar üretme işlemidir.
Elimizde 1 ve 2 noktaları varsa, araya 1.3, 1.6 gibi değerler hesaplanabilir.
"""

#Modül: scipy.interpolate

#1D İnterpolasyon: interp1d()
#Düzgün dağılımlı veriler için kullanılır.

from scipy.interpolate import interp1d
import numpy as np

xs = np.arange(10)
ys = 2*xs + 1  # Doğrusal: y = 2x + 1

interp_func = interp1d(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)



#Spline İnterpolasyonu: UnivariateSpline()   Spline = Parçalı polinom fonksiyonu
#Veriler düzgün dağılmamışsa veya eğri yapılıysa tercih edilir.
from scipy.interpolate import UnivariateSpline
import numpy as np

xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1  # Doğrusal olmayan

interp_func = UnivariateSpline(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)



#Radyal Tabanlı İnterpolasyon: Rbf()
#Dağınık (scatter) verilere uygundur. Tüm noktaları referans alır.
from scipy.interpolate import Rbf
import numpy as np

xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1

interp_func = Rbf(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)


"""
| Fonksiyon            | Amaç                                     | En Uygun Durum                    |
| -------------------- | ---------------------------------------- | --------------------------------- |
| `interp1d()`         | Basit doğrusal/interpolasyon             | Düzgün sıralı veriler             |
| `UnivariateSpline()` | Parçalı spline eğrileriyle interpolasyon | Doğrusal olmayan, pürüzlü veriler |
| `Rbf()`              | Radyal tabanlı enterpolasyon             | Dağınık, çok boyutlu veriler      |

"""
