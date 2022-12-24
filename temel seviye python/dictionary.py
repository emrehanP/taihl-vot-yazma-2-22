"""
Dictionary "anahtar", "değer" ikililerinden oluşur
    "ad": "Eren"
    "soyad": "Özdal"
"""

numaralar = [66, 75]
isimler = ["ahmet", "mehmet"]

numara = int(input("öğrenci numarasını yazınız : "))

konum = numaralar.index(numara)
print(isimler[konum])








ogrenciler = {66: "ahmet", 75: "mehmet"}
print(ogrenciler[numara])

kisiler = {

    1: {
        "ad": "eren",
        "soyad": "özdal",
        "cinsiyet": True,
        "dersler": ["türkçe"]
    },
    45: {
        "ad": "eren",
        "soyad": "özdal",
        "cinsiyet": True,
        "dersler": ["türkçe"]
    }

}

print(kisiler[45]["dersler"])










