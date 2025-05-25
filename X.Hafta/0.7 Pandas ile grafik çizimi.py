"""
Pandasta, diyagramlar oluşturmak için plot() yöntemini kullanır.
"""

"""
Diyagramı ekranda görselleştirmek için Matplotlib kütüphanesinin bir alt modülü olan
Pyplot'u kullanabiliriz
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')
df.plot()
plt.show()

"""
kind argümanıyla bir dağılım grafiği istediğinizi belirtin:
kind = 'scatter'

Bunun gibi x ve y argümanlarını ekleyin:
x = 'Duration', y = 'Calories'

"""
df = pd.read_csv('data.csv')
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()

#Sütunlar arasında hiçbir ilişkinin olmadığı bir dağılım grafiği:
df = pd.read_csv('data.csv')
df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
plt.show()


#Histogram grafiği için ise:
df["Duration"].plot(kind = 'hist')
