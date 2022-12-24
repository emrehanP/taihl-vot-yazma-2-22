liste = []
print(liste)
print(type(liste))

okul = "sancaktepe teknoloji anadolu imam hatip lisesi"
kelimeler = okul.split()
print(kelimeler)

#belirli  sıradaki kelimeler yazdıralım

print(kelimeler[0])
print(kelimeler[1])
print(kelimeler[2])
print(kelimeler[3])
print(kelimeler[4])
print(kelimeler[5])
print(kelimeler[-6])

ad = "devlet tayip kılıçdaroğlu imam peker"
print(ad[0])
print(ad[1])
print(ad[2])
print(ad[3])
print(ad[4])

print(ad[0:])

print(ad[::-1])

print(ad[0::-1])

print(ad[-7:-14:-1])

#LİSTELER İÇERİSİNDE FARKLI TÜRDEN VERİLER OLABİLİR

liste = [1, 12.3, "phthon" ,True, [1, 2, 3]]

print(liste[-1][-1])
print(liste[4][-1])



# iki listeyi birleştirme

liste2 = [1, 2, 3]
liste3 = [4, 5, 6]
liste4 = liste2 + liste3
liste5 = liste3 + liste2
print(liste4)
print(liste5)




