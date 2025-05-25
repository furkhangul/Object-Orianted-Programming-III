#JSon okuma işlemi için read_json fonkisyonu kullanılır.
import pandas as pd
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

#df = pd.read_json('data.json')
#print(df.to_string())


#Dictionary ifadesi ile de datafreme oluşturulabilir.

data = {
 "Duration":{
 "0":60,
 "1":60,
 "2":60,
 "3":45,
 "4":45,
 "5":60
 },
 "Pulse":{
 "0":110,
 "1":117,
 "2":103,
 "3":109,
 "4":117,
 "5":102
},
 "Maxpulse":{
 "0":130,
 "1":145,
 "2":135,
 "3":175,
 "4":148,
 "5":127
 },
 "Calories":{
 "0":409,
 "1":479,
 "2":340,
 "3":282,
 "4":406,
 "5":300
}
}
data1 = pd.DataFrame(data)
print(data)
print()

#ilk 10 veriyi görmek için head() fonkisiyonu kullanılır.
csv = pd.read_csv("ornek.csv")
print(csv.head(10))

#Defaultta ilk 5 veriyi veriyor
print()
print(csv.head())

#Son 5 satırı görmek için ise tail() fonkisyonu kullanılır.
print()
print(csv.tail())

#Data hakkında bilgi almak için ise info() fonksiyonu kullanılır.
print()
print(csv.info())
