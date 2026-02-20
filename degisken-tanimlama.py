urunAFiyat= 4000
urunBFiyat= 3000
kdvOrani= 0.20

print( urunAFiyat + (urunAFiyat * kdvOrani) ) 
#print("Ürün B Fiyati: " + urunBFiyat +(urunBFiyat * kdvOrani))
#böyle bir ifade yazamam, sayı ile string direkt toplanmaz .
#1.yol: str kullanmaktır.sayıyı string’e çevirmek gerekir
print( "Ürün A kdvli Fiyati: " + str (urunAFiyat + (urunAFiyat * kdvOrani) )) 
#2. yol: (f-string)
print(f"Ürün B kdvli Fiyati: {urunBFiyat + (urunBFiyat * kdvOrani)}")

print( "Ürünlerin KDVsiz toplamlari: "+ str(urunAFiyat + urunBFiyat))
print( "Ürünlerin KDVli toplamlari: "+ str((urunAFiyat+ urunAFiyat *kdvOrani) + (urunBFiyat + urunBFiyat * kdvOrani)))
