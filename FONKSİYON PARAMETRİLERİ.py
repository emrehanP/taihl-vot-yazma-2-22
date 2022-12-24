def ogrenci_kaydet(ad, soyad, notlar):
    notlar_list = [int(x) for x in notlar.split(",")]
    ortalama = sum(notlar_list) / len(notlar_list)


    dosya = open("öğrenciler.txt", mode="r", encoding="utf-8")
    dosya.write(f"ad: {ad}, soyad: {soyad}, notlar: {notlar}, ortalama: {ortalama}\n")
    dosya.close()


def ogrenci_kaydet2(ad, soyad, notlar=None):
    if notlar:

        notlar_list = [int(x) for x in notlar.split(",")]
        ortalama = sum(notlar_list) / len(notlar_list)
    else:
        notlar = "not bilgisi yok"
        ortalama = "ortalama hesaplanamadı"

    dosya = open("öğrenciler.txt", mode="a", encoding="utf-8")
    dosya.write(f"ad: {ad}, soyad: {soyad}, notlar: {notlar}, ortalama: {ortalama}\n")
    dosya.close()

while True:
    ne_yapilacak = input("ne yapacaksınız? (1: kaydet, 0: çık):")

    if ne_yapilacak == "0":
        break
    ad = input("oğrenci adı: ")
    soyad = input("oğrenci soyadı: ")
    notlar = input("sınav notları (virgülle ayrılmış): ")
    if notlar != "":
        ogrenci_kaydet2(ad, soyad, notlar)
    else:
        ogrenci_kaydet2(ad, soyad)





