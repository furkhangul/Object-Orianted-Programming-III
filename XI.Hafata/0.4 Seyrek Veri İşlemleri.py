#Seyrek Veri İşlemleri
"""
Seyrek veri, çoğunluğu sıfırlardan oluşan veridir.
Örnek:
[1, 0, 2, 0, 0, 3, 0, 0, 0]

Karşıtı: Yoğun Veri (Dense Data)
Değerlerin çoğu 0 dışıysa buna yoğun veri den


Neden kullanılır:

Büyük veri setlerinde her öğeyi (özellikle sıfırları) saklamak hem bellek hem de işlem süresi açısından verimsizdir.
Seyrek matrisler:
Bellekten tasarruf sağlar
Matematiksel işlemleri hızlandırır
"""

"""
SciPy, scipy.sparse modülü ile bu tür verileri işler.
En yaygın kullanılan 2 tür seyrek matris şunlardır:

Tür	Açıklama
CSR	Compressed Sparse Row – Hızlı satır işlemleri ve matris-çarpım işlemleri
CSC	Compressed Sparse Column – Hızlı sütun işlemleri
"""

#CSR Matrisi
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
print(csr_matrix(arr))

#.data: Sıfır olmayan elemanları gösterir
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
mat = csr_matrix(arr)
print(mat.data)  # [1 1 2]

#.count_nonzero(): Kaç tane sıfır olmayan eleman var olduğunu gösterir.
print(mat.count_nonzero())  # 3

#.eliminate_zeros(): Gereksiz sıfırları siler (önceden 0 olarak atanmış olabilir)
mat.eliminate_zeros()
print(mat)

#.sum_duplicates(): Aynı pozisyondaki girişler varsa toplar. Kopya değerlerin toplamını alır ve yinelenmeleri kaldırır.
mat.sum_duplicates()

#.tocsc(): CSR → CSC dönüşümü. Sütun bazlı bir matris işlemine ihtiyaç varsa kullanılabilir:
csc_mat = mat.tocsc()
print(csc_mat)

