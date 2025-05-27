#SciPy' Kütüphanesinde Sabitler

"""
SciPy kütüpühanesinde daha çok bilimsel uygulamalara odaklandığı için, bir çok yerleşik sabit bulunmaktadır.
Bu sabitler, Veri Bilimi ile çalışırken yardımcı olabilir.
Bunun için constants kitaplığı kullanılır.
"""

from scipy import constants

#PI sabiti için
print(constants.pi)

#Constants kitaplığınındaki fonksiyonları görmek için dir() fonksiyonu çalıştırılır.
print(dir(constants))

#Metrik işlemler
#Kullanım alanları: uzunluk, kütle, hacim vb. metrik sistemde ifade edilen ölçümler.
#Belirtilen birimi metre (meter) cinsinden döndür (ör. centi, 0.01 döndürür)
print(constants.kilo)  # 1000.0
print(constants.centi)  # 0.01



#Binary (İkili) İşlemler
#Kullanım alanları: MB, GB, TB gibi belleği ölçerken.
#Belirtilen birimi bayt (bytes) cinsinden döndür (ör. kibi, 1024'ü döndürür)
print(constants.mebi)  # 1048576
print(constants.gibi)


#Kütle işlemleri
#Kullanım alanları: fizik, mühendislik, kimya.
#Belirtilen birimi kg cinsinden döndürür (örneğin, gram 0,001 döndürür)
print(constants.lb)  # 0.45359236999999997

#Açı İşlemleri
#Açıları radyan cinsinden ifade eder.
#Kullanım alanları: trigonometrik hesaplamalar, mühendislik, astronomi.
#degree → 1 derece = 0.01745 radyan
print(constants.degree)  # 0.017453...


#Zaman İşlemleri
#Saniye cinsinden zaman dönüşümleri sağlar.
#Kullanım alanları: fizik, zaman hesaplamaları, programlama.
#Belirtilen birimi saniye cinsinden döndür (ör. hour 3600.0 değerini döndürür)
print(constants.hour)  # 3600.0

#UzunluK İşlemleri
#Birimleri metreye çevirir.
#Kullanım alanları: ölçüm, mühendislik, coğrafya, fizik.
#Belirtilen birimi metre cinsinden döndür (ör. nautical_mile, 1852,0 değerini döndürür)
print(constants.mile)  # 1609.343999...


#Basınç İşlemleri
#Birimleri paskal (Pa) cinsinden verir.
#Kullanım alanları: meteoroloji, mühendislik, fizik.
#Belirtilen birimi paskal cinsinden döndür (ör. psi, 6894.757293168361) değerini döndürür
print(constants.psi)  # 6894.757...


#Alan İşlemleri
#Birimleri metrekareye çevirir.
#Kullanım alanları: tarım, harita mühendisliği, şehir planlama.
#Belirtilen birimi metrekare cinsinden döndür (ör. hectare, 10000.0 döndürür)
print(constants.acre)  # 4046.856422...


#Hacim İşlemleri
#Birimleri metreküpe çevirir.
#Kullanım alanları: sıvı hacmi ölçümleri, kimya, ticaret.
#Belirtilen birimi metreküp cinsinden döndür (ör. liter 0,001 döndürür)

print(constants.gallon)  # 0.003785...

#Hız İşlemleri
#Hız birimlerini metre/saniye olarak ifade eder.
#Kullanım alanları: mekanik, uçuş hesaplamaları, trafik analizi.
#Belirtilen birimi saniye başına metre cinsinden döndür (ör. speed_of_sound, 340,5 değerini döndürür)
print(constants.mph)  # 0.44704


#Sıcaklık İşlemleri
#Sıcaklık birimlerini Kelvin cinsine çevirir.
#Kullanım alanları: fizik, meteoroloji, termodinamik.
print(constants.zero_Celsius)  # 273.15

#Enerji İşlemleri
#Enerji birimlerini joule cinsinden verir.
#Kullanım alanları: termodinamik, nükleer enerji, elektrik.
#Belirtilen birimi joule cinsinden döndür (ör. kalori dönüşü 4.184)
print(constants.hp)  # 745.699...


#Güç İşlemleri
#Gücü watt cinsinden ifade eder.
#Kullanım alanları: elektrik gücü, motor gücü, enerji sistemleri.
#Belirtilen birimi watt cinsinden döndür (ör. horsepower 745,998715822701)
print(constants.hp)  # 745.699...



#Kuvvet İşlemleri
#Kuvveti Newton (N) cinsinden verir.
#Kullanım alanları: mekanik, yapı mühendisliği, fizik.
#Belirtilen birimi Newton cinsinden döndür (ör. kilogram_force, 9.80665 değerini döndürür)
print(constants.kgf)  # 9.80665


"""
Kategori	        Ölçü Birimi   	Dönüşüm Sağladığı Birim
Kütle (mass)	    gram, lb, ton	    kilogram (kg)
Uzunluk (length)	inch, mile, au	    metre (m)
Zaman (time)	    minute, day	        saniye (s)
Basınç (pressure)	psi, atm	        paskal (Pa)
Hacim (volume)  	liter, gallon	    metreküp (m³)
Enerji (energy)	    calorie, eV	        joule (J)
Kuvvet (force)	    lbf, kgf	        newton (N)
"""
