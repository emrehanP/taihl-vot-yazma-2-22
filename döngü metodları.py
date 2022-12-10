liste = list(range(1, 10))
print(liste)

for sayi in range(51):
    print(f"{sayi}.python")



kelime = "pyton"
kelime_enum = list(enumerate(kelime))
print(kelime_enum)

for i, harf in kelime:
    print(harf)




sayilar = [1, 2, 4]
okunuslar = ["bir","iki","dört"]



sayilar_zip = zip(sayilar, okunuslar)
for sayi, okunuslar in zip(sayilar, okunuslar):
    print(sayilar, okunuslar)










