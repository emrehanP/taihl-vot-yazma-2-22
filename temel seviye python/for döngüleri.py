ogrenciler = ["ömer, murat, kerem, abrudthana"]


for ogrenci in ogrenciler:
    print(f"öğrencinin adı: {ogrenci}")


sayilar = [(1, 2), (3, 4), (5, 6)]

for a, b in sayilar:
    print(f"1.sayi: {a}, 2. sayı: {b}")

okul = "sancaktepe teknoloji anadolu imam hatip lisesi"

for kelime in okul.split():
    print(f"okul: {kelime}")


ogrenciler = {

    1: {
        "ad": "eren",
        "soyad": "özdal",
        "cinsiyet": True,
        "dersler": ["türkçe"]
    },
    45: {
        "ad": "ıgıtrınıs",
        "soyad": "özdal",
        "cinsiyet": True,
        "dersler": ["türkçe"]
    }

}

for no, ogrenci in ogrenciler.items():
    print(f"{no} numaralı ogrenci: {ogrenci['ad']}")

























