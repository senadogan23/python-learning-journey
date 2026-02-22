"""
Aşağıdaki  müşterinin bilgilerini ve satın aldığı ürün bilgilerini değişkenler içinde saklayınız.
Toplam ödenen ücret nedir?
Ödenen miktarın kdv oranı nedir?(%18)

Sena Doğan
05230232323 
info@senadogan.com
Elazığ

Satın Alınan Ürünler

Ürün Adı: Kablosuz Mouse 
Fiyatı: 550 tl

Ürün Adı:Kablosuz Klavye
Fiyatı: 650tl

Ürün Adı: Dizüstü Bilgisayar
Fiyatı: 55.000 TL

"""
adSoyad= "Sena Doğan"
telNo= 5230232323
mail= "info@senadogan.com"
adres= "Elazığ"

urun1=550
urun2=650
urun3=55000

toplamUrunFiyati = urun1 + urun2 + urun3
toplamKdvOrani= (toplamUrunFiyati * 0.18)

print(adSoyad + " kişisinin " + str(telNo) + " numarası ile "+  mail + " mail hesabından "+ 
       adres+  " adresine "+ str(toplamUrunFiyati) +" tl sipariş alınmıştır. Toplam kdv oranı ile alınan ücret: " +str(toplamKdvOrani))