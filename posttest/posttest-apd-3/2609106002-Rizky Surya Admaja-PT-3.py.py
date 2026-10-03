print("========================================")
print("          SELAMAT DATANG                ")
print("        KASIR TIKET BIOSKOP             ")
print()
 
nama = input("Nama pembeli: ")
umur = int(input("Umur pembeli: "))
jenis_tiket = input("Jenis tiket (Reguler/Premium/VIP): ")
member = input("Status member (Ya/Tidak): ")
bayar = int(input("Nominal uang bayar: "))
 
if umur < 13:
    print("Mohon maaf, anda belum cukup umur untuk menonton")
else:
    if jenis_tiket == "Reguler":
        harga = 50000
    elif jenis_tiket == "Premium":
        harga = 75000
    elif jenis_tiket == "VIP":
        harga = 100000
    else:
        harga = 0
 
    if harga == 0:
        print("Jenis tiket tidak valid")

    else:
        diskon = harga * 0.2 if member == "Ya" else 0
        admin = 0 if member == "Ya" else 2000
        total = harga - diskon + admin
 
        if bayar < total:
            print("Uang bayar kurang, total yang harus dibayar:", total)
        else:
            kembalian = bayar - total
 
            print("")
            print("======================================")
            print("            TIKET NONTON              ")
            print("======================================")
            print("Pembeli   :", nama)
            print("Umur      :", umur)
            print("Tiket     :", jenis_tiket)
            print("Member    :", member)
            print("======================================")
            print("Harga awal   : Rp", harga)
            print("Potongan     : Rp", diskon)
            print("Biaya admin  : Rp", admin)
            print("Harus dibayar: Rp", total)
            print("Dibayar      : Rp", bayar)
            print("Kembali      : Rp", kembalian)
            print("======================================")
            print("          SELAMAT NONTON              ")
            print("           TERIMA KASIH               ")