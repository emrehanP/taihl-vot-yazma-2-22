# sayi = 0
# while sayi < 100:
#     print(sayi)
#
#
#     sayi += 1
#
#     if sayi % 2 == 0:
#         print(f"{sayi} çift sayıdır.")
#
#
#     else:
#         print(f"{sayi} tek seyıdır.")
#
#
#     sayi += 1


import xlrd

ck = xlrd.open_workbook("veriler/WorldCupPlayers.xls")

cs = ck.sheet_by_index(0)




satir_siyisi = cs.nrows
sutun_syisi = cs.ncols
print(f"satır sayısı: {satir_siyisi}")
print(f"sutün sayısı: {sutun_syisi}")


a1 = cs.cell(0, 0)
print(a1)

satir = 1

while satir < satir_siyisi:
    futbolcu = cs.cell_value(satir, 6)


    if futbolcu.startswith("R"):
        print(f"futbolcu: {futbolcu}")
    olay = cs.cell_value(satir, 8)
    if olay != "":
        print(f"futbolcu: {futbolcu} - olay: {olay}")



    satir += 1














