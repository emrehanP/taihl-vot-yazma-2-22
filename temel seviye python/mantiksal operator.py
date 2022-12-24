"""
MANTIKSAL OPERATÖRLER
//////////////////////////////////////////////////////////////////////////////
Python'da birden fazla koşulu beraber değerlendirmek için kullanırız.
+----------+----------+-----------------+
| Operatör | Açıklama |    Kullanımı    |
+----------+----------+-----------------+
|    and   | ve       | (x<y) and (a>b) |
+----------+----------+-----------------+
|    or    | veya     |  (x<y) or (a>b) |
+----------+----------+-----------------+
|    not   | değil    |    not (x<y)    |
+----------+----------+-----------------+
"""

futbolcu1 = {
    "gol": 5,
    "asist": 566,
}
futbolcu2 = {
    "gol": 8,
    "asist":3
}

print(f"1.futbolcu: {(futbolcu1['gol']) > 5 and (futbolcu1['asist'] > 8)}")
print(f"2.futbolcu: {(futbolcu2['gol']) > 5 and (futbolcu2['asist'] > 8)}")


































































