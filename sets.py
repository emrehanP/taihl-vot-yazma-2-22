"""
sets listeleri süslü parantezler '{}' içinde tanımlanır.
sets liste elemanlarına indeks numaraları ile ulaşılamaz.
sets liste elemanlarına döngü içinde ulaşılır.
sets listeleri içinde aynı eleman birden fazla yer alamaz.
"""

# sets listesi oluşturalım
sets_liste = {1, 2, 3, 4}



# sets listenin içindeki bir elemanı ulaşalım
# print(sets_liste[0])

for eleman in sets_liste:
    print(eleman)

sets_liste.add(5)
print(sets_liste)


sets_liste.update([19,20,21,31,370535935304530456356563567395])
print(sets_liste)

liste = [1, 2, 3, 4, 6, 578, 397463485730975395345763587963495876395783563975356736776675435796376576539756937563467856347869534756356853768385976378465346367537568]
sets_liste = set(liste)
print(sets_liste)


















































































































































