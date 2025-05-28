#Optimizasyon Modülü

"""
SciPy'nin optimize modülü, matematiksel fonksiyonların köklerini bulmak, minimum veya maksimum noktalarını tespit etmek gibi problemleri çözmek için kullanılır.
Bu, hem bilimsel hesaplamalarda hem de Makine Öğrenmesi gibi alanlarda çok önemlidir.
"""

#Optimizasyon
"""
SciPy.optimize, fonksiyonları optimize etmek için çeşitli araçlar sunar.
Özellikle şu işlemler için kullanılır:

*Bir fonksiyonun minimum (en küçük) değerini bulmak

*Bir denklemin kökünü (sonucunun 0 olduğu x değeri) bulmak

*Eğriler üzerinde global ve lokal minimum/maksimum noktaları belirlemek
"""

#Denklemin Kökünü Bulmak (root)
from scipy.optimize import root
import numpy as np

def formul(x):
    return x + x**2 + np.cos(x)

sonuc = root(formul, 10)
print(f"Sonuç: {sonuc.x}")


#Fonskiyonları minimize etmek:
from scipy.optimize import minimize
def fun(x):
    return x**2 + 4*x + 4
sonuc = minimize(fun, 0, method="BFGS")
print(f"Sonuç: {sonuc.x}")

"""
fun: Fonksiyon 

x0: Başlangıç değeri

method: Hangi optimizasyon algoritmasının kullanılacağı (BFGS, CG, TNC vb.)

options: Ek ayarlar (örneğin disp=True ile detaylı çıktı almak)
"""

"""
Terim	    Anlamı
root()	    𝑓(𝑥)=0 f(x)=0 olacak şekilde 
𝑥           x'i bulur (kök)
minimize()	Fonksiyonun en küçük değerini ve bu değere karşılık gelen x'i bulur
method	    Kullanılan optimizasyon algoritması
x0	        Tahminle başlamak için ilk değer
"""
