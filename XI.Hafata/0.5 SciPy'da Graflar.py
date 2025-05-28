#SciPy'da Graflar

"""
SciPy, çizge işlemleri için scipy.sparse.csgraph modülünü kullanır.
Bu modülle komşuluk (adjacency) matrisleri üzerinden çizge işlemleri yaparız.
"""

# connected_components() Grafikteki bağlı alt grupları (connected components) bulur.
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
import numpy as np

arr = np.array([
    [0, 1, 2],
    [1, 0, 0],
    [2, 0, 0]
])
graph = csr_matrix(arr)

n_components, labels = connected_components(graph)
print(n_components)  # Kaç grup var?
print(labels)        # Hangi düğüm hangi grupta

#dijkstra() Bir noktadan diğerlerine olan en kısa yolu bulur.
from scipy.sparse.csgraph import dijkstra

distances, predecessors = dijkstra(graph, indices=0, return_predecessors=True)
print(distances)      # 0. düğümden diğerlerine uzaklık
print(predecessors)   # Hangi düğümden geldiğini gösterir

# floyd_warshall() Tüm düğüm çiftleri arasındaki en kısa yolları verir.
from scipy.sparse.csgraph import floyd_warshall

distances, predecessors = floyd_warshall(graph, return_predecessors=True)
print(distances)

#bellman_ford() Negatif ağırlıkları da destekleyen en kısa yol algoritmasıdır.
from scipy.sparse.csgraph import bellman_ford

arr = np.array([
    [0, -1, 2],
    [1, 0, 0],
    [2, 0, 0]
])
graph = csr_matrix(arr)

distances, predecessors = bellman_ford(graph, indices=0, return_predecessors=True)
print(distances)


#depth_first_order() Verilen bir düğümden başlayarak derinlik öncelikli (DFS) şekilde gezer.
from scipy.sparse.csgraph import depth_first_order

arr = np.array([
    [0, 1, 0, 1],
    [1, 1, 1, 1],
    [2, 1, 1, 0],
    [0, 1, 0, 1]
])
graph = csr_matrix(arr)

node_order, predecessors = depth_first_order(graph, 1)
print(node_order)

#breadth_first_order() Verilen bir düğümden başlayarak genişlik öncelikli (BFS) gezer.

from scipy.sparse.csgraph import breadth_first_order

node_order, predecessors = breadth_first_order(graph, 1)
print(node_order)
"""
Kullanım Alanları:
Uygulama	                Kullanım Alanı
Harita/Yol Uygulamaları	    En kısa rota bulma (Google Maps gibi)
Sosyal Ağ Analizi	        Kimin kiminle bağlantılı olduğunu bulma
Web Tarama	                Bağlantılı sayfaları keşfetme (Google Bot)
Veri Kümeleme	            Bağlı bileşenlere ayırma
Elektrik Şebekeleri	        Ağ üzerinde geçiş hesaplama
"""
