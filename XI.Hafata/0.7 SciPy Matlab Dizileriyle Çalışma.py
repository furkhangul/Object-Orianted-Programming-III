#SciPy Matlab Dizileriyle Çalışma
"""
SciPy, scipy.io modülü ile Matlab .mat dosyalarıyla kolayca veri alışverişi yapmamıza olanak tanır.
"""

#Matlab Formatında Veri Dışa Aktarma

"""
Fonksiyon: savemat(filename, mdict, do_compression=False)

Açıklamalar:
filename: Kaydedilecek .mat dosyasının adı.

mdict: Kaydedilecek verilerin bulunduğu Python sözlüğü (dict).

do_compression: Dosya sıkıştırılsın mı? (varsayılan: False)
"""
from scipy import io
import numpy as np

arr = np.arange(10)
io.savemat('arr.mat', {"vec": arr})  # vec isimli değişken olarak kaydet

#Bilgisayarda bir arr.mat dosyası oluşur.

#Matlab Formatındaki Verileri İçe Aktarma
"""
Fonksiyon: loadmat(filename)
"""
from scipy import io

# Dosyayı içe aktar
mydata = io.loadmat('arr.mat')

print(mydata)

#Diziyi Tek Boyuta İndirme
"""
Yüklenen dizinin fazladan bir boyutu varsa, bunu tek boyuta (1D) indirmek için squeeze_me=True kullanın.
"""
mydata = io.loadmat('arr.mat', squeeze_me=True)
print(mydata['vec'])  # Artık 1D: [0 1 2 ... 9]

"""
İşlem	                                Fonksiyon	                Açıklama
Matlab dosyasına veri kaydetme	        savemat()	                .mat dosyası oluşturur
Matlab dosyasını okuma	                loadmat()	                Python sözlüğü döner
Dizi sıkıştırma (tek boyuta indirme)	squeeze_me=True	            Gereksiz boyutları temizler
"""
