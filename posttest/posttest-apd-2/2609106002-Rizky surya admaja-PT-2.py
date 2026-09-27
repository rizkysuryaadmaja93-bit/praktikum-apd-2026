barang_1 = 15000
barang_2 = 25000
barang_3 = 10000
barang_4 = 5500
barang_5 = 5000
barang_6 = 20000

print('barang_1 =',barang_1)
print('barang_2 =',barang_2)
print('barang_3 =',barang_3)
print('barang_4 =',barang_4)
print('barang_5 =',barang_5)
print('barang_6 =',barang_6)

barang = [barang_1, barang_2, barang_3, barang_4, barang_5, barang_6]
total_bayar = barang_1 + barang_2 + barang_3 + barang_4 + barang_5 + barang_6

pajak = total_bayar * 15 / 100
total_belanja = total_bayar + pajak
rata_rata = total_bayar / len(barang)

mata_uang_EUR = 20.466
mata_uang_RM = 4.362

EUR = total_belanja / mata_uang_EUR
RM = total_belanja / mata_uang_RM


nim = 2
bolean = nim < rata_rata

print()
print(' Koprasi Desa Merah Putih  ')
print(' Hasil Belanja ')

print()
print('barang =',barang)
print('total_bayar =',total_bayar)
print('pajak =',pajak)
print('total_belanja =',total_belanja)
print('rata_rata =',rata_rata)
print('nim =',nim)
print('bolean =',bolean)
print('EUR =',EUR)
print('RM =',RM)
print("List Slicing:",barang[1:6:2])