#SciPy Uzamsal Veriler

"""
Uzamsal veriler, genellikle noktalar, koordinatlar, mesafeler ve geometrik yapılarla ilgilidir.
SciPy'nin scipy.spatial modülü, bu verilerle çalışma, ölçüm yapma ve analiz etme konusunda birçok güçlü araç sunar.
"""

#Üçgenleme

"""
Amaç: Noktalar arasındaki düzlemi üçgenlere bölmek.

Kullanılan Yöntem: Delaunay()
"""

import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

points = np.array([
    [2, 4],
    [3, 4],
    [3, 0],
    [2, 2],
    [4, 1]
])
triangles = Delaunay(points)

plt.triplot(points[:, 0], points[:, 1], triangles.simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')
plt.show()


#Dışbükey Örtü
"""
Amaç: Noktaları çevreleyen en küçük dışbükey çokgeni bulmak.
Kullanılan Yöntem: ConvexHull()
"""
from scipy.spatial import ConvexHull

points = np.array([
    [2, 4], [3, 4], [3, 0], [2, 2], [4, 1],
    [1, 2], [5, 0], [3, 1], [1, 2], [0, 2]
])
hull = ConvexHull(points)

plt.scatter(points[:, 0], points[:, 1])
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
plt.show()

#KDTree
"""
Amaç: Bir noktaya en yakın olan diğer noktayı hızlıca bulmak.
Kullanılan Yöntemler: KDTree(), .query()
"""

from scipy.spatial import KDTree

points = [(1, -1), (2, 3), (-2, 3), (2, -3)]
tree = KDTree(points)

distance, index = tree.query((1, 1))  # (1,1) noktasına en yakın komşu
print(distance, index)

#Mesafe Ölçümleri
"""
Euclidean (Öklid) Mesafesi
Klasik düz çizgi mesafesi.
"""
from scipy.spatial.distance import euclidean

p1 = (1, 0)
p2 = (10, 2)
print(euclidean(p1, p2))  # 9.21


#Cityblock (Manhattan) Mesafesi
"""
Sadece yukarı, aşağı, sağ, sol adımlarla ölçüm.
"""

from scipy.spatial.distance import cityblock

print(cityblock(p1, p2))  # 11

# Cosine Mesafesi
"""
İki vektör arasındaki açının kosinüs değeri.
"""
from scipy.spatial.distance import cosine

print(cosine(p1, p2))  # 0.019

#Hamming Mesafesi

"""
Bit düzeyinde fark oranı (örn. ikili diziler arasında kaç farklı bit var?).
"""

from scipy.spatial.distance import hamming

p1 = (True, False, True)
p2 = (False, True, True)
print(hamming(p1, p2))  # 0.666...
"""
Uygulama	                        Açıklama
Coğrafi Bilgi Sistemleri (GIS)	    Koordinatlarla alan ve konum analizi
Makine Öğrenimi	                    En yakın komşu, kümeleme, mesafe temelli modeller
Bilgisayar Grafikleri	            Çokgen bölme, dış sınır çizimi
Oyun ve Simülasyonlar	            En kısa yol, komşu kontrolü, alan hesaplama
"""


"""
Yöntem/Kavram	    Açıklama
Delaunay	        Noktalardan üçgenler oluşturur
ConvexHull	        Noktaları çevreleyen dışbükey çokgen
KDTree	            En yakın komşu bulma
euclidean()	        Doğrusal (düz çizgi) mesafe
cityblock()	        Adım (Manhattan) mesafesi
cosine()	        Açıya dayalı uzaklık
hamming()	        İkili fark oranı

"""
