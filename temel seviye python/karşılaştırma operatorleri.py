"""
KARŞILAŞTIRMA OPERATÖRLERİ
//////////////////////////////////////////////////////////////////////////////
Python'da değişkenlerin içindeki verileri karşılaştırmak için kullanırız
+----------+----------------+-----------+
| Operatör | Açıklama       | Kullanımı |
+----------+----------------+-----------+
|    ==    | eşit mi?       |   x == y  |
+----------+----------------+-----------+
|    !=    | eşit değil mi? |   x != y  |
+----------+----------------+-----------+
|     >    | büyük mü?      |   x > y   |
+----------+----------------+-----------+
|     <    | küçük mü?      |   x < y   |
+----------+----------------+-----------+
|    >=    | büyük eşit mi? |   x >= y  |
+----------+----------------+-----------+
|    <=    | küçük eşit mi? |   x <= y  |
+----------+----------------+-----------+
"""

kullanici_adi = "ebdurrahman"
sifre = "1234"


k_adi = input("kullanıcı adını gir: ")
k_sifre = input("sifrenizi yazınız: ")


print(f"kullanıcı adın dogrumu: {kullanici_adi == k_adi}")
print(f"sifre yanlıs mu: {sifre == k_sifre }")



yas1 = 36
yas2 = 35
print("büyük mü: " + str(yas1 > yas2))
print("küçükmü: {}" .format(yas2 < yas1))





