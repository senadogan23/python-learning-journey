"""
Uygulama 1: Yarıçapı verilen bir dairenin alan ve çevresini hesaplayınız.
Alan: pi*r*r
Çevre: 2*pi*r

Uygulama 2: Klavyeden girilen km bilgisini mil cinsinden hesaplayınız
mil= km/1.609344

"""
pi= 3.14
r=10
print("10 yarıçaplı dairenin alanı: "+str(pi*r*r) )

print("10 yarıçaplı dairenin çevresi: "+ str(2*pi*r))

yaricap= float(input("Alan ve çevresini hesaplamak istediğiniz dairenin yarıçapını giriniz: " ))
alan =pi*yaricap*yaricap #pi *(r ** 2) ifadesi de kullanılabilir
cevre= 2*pi*yaricap

print("Alanı: "+str(alan)+ " Çevresi: "+str(cevre))

km=float(input("mil'e çevirmek istediğiniz km bilgisini giriniz: "))
mil=km/1.609344
print(mil)


#hocanın çözümü aşağıdaki gibiydi: 
mesafeKm=input("km: ")
mesafeMil=float(mesafeKm)/ 1.609344
mesafeMil= round(mesafeMil, 2)
print(mesafeKm + " km: " + str(mesafeMil)+ " mil")