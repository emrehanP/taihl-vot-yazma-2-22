#kullanıcıdan iki sayı alalım
# örnek = 1. sayı (5), 2.sayıdan (3) büyüktür
# örnek = 2. sayı (9), 1.sayıdan (4) büyüktür


sayi1 = int(input("1. sayıyı yazın: "))
sayi2 = int(input("2. sayıyı yazın: "))



if sayi1 > sayi2:
    print(f"1. sayı ({sayi1}), 2.sayıdan ({sayi2}) büyüktür.")
elif sayi2 > sayi1:
    print(f"2. sayı ({sayi2}), 1.sayıdan ({sayi1}) büyüktür.")
else:
    print(f"1. sayı ({sayi1}), 2.sayıya ({sayi2}) eşittir.")

















