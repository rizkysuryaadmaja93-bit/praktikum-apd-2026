akun = [["admin1", "admin123", "admin"], ["surya", "surya123", "user"], ["admin2", "admin456", "admin"], ["rizky", "rizky456", "user2"]]


pesanan = [
    ["surya", "Skripsi", 100, 1, "Hitam Putih", 100000, "Diproses"],
    ["rizky", "Poster", 5, 1, "Warna", 10000, "Selesai"]
]

jenis = ("Hitam Putih", "Warna")
harga = (1000, 2000)

angka = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

while True:
    print()
    print("=== PENGHITUNG BIAYA CETAK DOKUMEN ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        user = input("Username: ")
        pw = input("Password: ")
        role = ""
        for a in akun:
            if a[0] == user and a[1] == pw:
                role = a[2]

        if role == "":
            print("Username atau password salah!")

        elif role == "admin":
            print("Login berhasil, halo admin")
            while True:
                print()
                print("=== MENU ADMIN ===")
                print("1. Tambah pesanan")
                print("2. Lihat pesanan")
                print("3. Ubah pesanan")
                print("4. Hapus pesanan")
                print("5. Logout")
                menu = input("Pilih menu: ")

                if menu == "1":
                    nama = input("Nama pemesan: ")
                    dok = input("Jenis dokumen: ")
                    hal = input("Jumlah halaman: ")
                    rkp = input("Jumlah rangkap: ")
                    print("1. Hitam Putih (Rp1000 per lembar)")
                    print("2. Warna (Rp2000 per lembar)")
                    jns = input("Pilih jenis cetak: ")

                   
                    benar = True
                    for c in hal + rkp:
                        cocok = False
                        for d in angka:
                            if c == d:
                                cocok = True
                        if cocok == False:
                            benar = False
                    if hal == "" or rkp == "":
                        benar = False
                    if nama == "" or dok == "":
                        print("Data tidak boleh kosong!")
                    elif benar == False:
                        print("Halaman dan rangkap harus angka!")
                    elif int(hal) == 0 or int(rkp) == 0:
                        print("Halaman dan rangkap minimal 1!")
                    elif jns != "1" and jns != "2":
                        print("Pilihan jenis cetak salah!")
                    else:
                        total = int(hal) * int(rkp) * harga[int(jns) - 1]
                        pesanan.append([nama, dok, int(hal), int(rkp), jenis[int(jns) - 1], total, "Diproses"])
                        print("Pesanan berhasil ditambahkan")
                        print("Total biaya: Rp", total)

                elif menu == "2":
                    if len(pesanan) == 0:
                        print("Belum ada pesanan")
                    else:
                        pendapatan = 0
                        no = 1
                        for p in pesanan:
                            print("No:", no)
                            print("Nama:", p[0])
                            print("Dokumen:", p[1])
                            print("Halaman:", p[2])
                            print("Rangkap:", p[3])
                            print("Jenis cetak:", p[4])
                            print("Total biaya: Rp", p[5])
                            print("Status:", p[6])
                            print()
                            if p[6] == "Selesai":
                                pendapatan = pendapatan + p[5]
                            no += 1
                        print("Total pendapatan: Rp", pendapatan)

                elif menu == "3":
                    if len(pesanan) == 0:
                        print("Belum ada pesanan")
                    else:
                        for i in range(len(pesanan)):
                            print(i + 1, pesanan[i][0], pesanan[i][1], pesanan[i][6])
                        no = input("Nomor pesanan yang mau diubah: ")

                        i = -1
                        for n in range(len(pesanan)):
                            if no == str(n + 1):
                                i = n

                        if i == -1:
                            print("Nomor tidak ada!")
                        else:
                            print("1. Jumlah halaman")
                            print("2. Jumlah rangkap")
                            print("3. Jenis cetak")
                            print("4. Status")
                            ubah = input("Mau ubah yang mana: ")

                            if ubah == "1":
                                baru = input("Halaman baru: ")
                                benar = True
                                for c in baru:
                                    cocok = False
                                    for d in angka:
                                        if c == d:
                                            cocok = True
                                    if cocok == False:
                                        benar = False
                                if baru == "" or benar == False:
                                    print("Input harus angka!")
                                elif int(baru) == 0:
                                    print("Input minimal 1!")
                                else:
                                    pesanan[i][2] = int(baru)
                                    print("Data berhasil diubah")
                            elif ubah == "2":
                                baru = input("Rangkap baru: ")
                                benar = True
                                for c in baru:
                                    cocok = False
                                    for d in angka:
                                        if c == d:
                                            cocok = True
                                    if cocok == False:
                                        benar = False
                                if baru == "" or benar == False:
                                    print("Input harus angka!")
                                elif int(baru) == 0:
                                    print("Input minimal 1!")
                                else:
                                    pesanan[i][3] = int(baru)
                                    print("Data berhasil diubah")
                            elif ubah == "3":
                                print("1. Hitam Putih")
                                print("2. Warna")
                                baru = input("Pilih: ")
                                if baru == "1" or baru == "2":
                                    pesanan[i][4] = jenis[int(baru) - 1]
                                    print("Data berhasil diubah")
                                else:
                                    print("Pilihan salah!")
                            elif ubah == "4":
                                print("1. Diproses")
                                print("2. Selesai")
                                baru = input("Pilih: ")
                                if baru == "1":
                                    pesanan[i][6] = "Diproses"
                                    print("Data berhasil diubah")
                                elif baru == "2":
                                    pesanan[i][6] = "Selesai"
                                    print("Data berhasil diubah")
                                else:
                                    print("Pilihan salah!")
                            else:
                                print("Pilihan salah!")

                            if pesanan[i][4] == jenis[0]:
                                pesanan[i][5] = pesanan[i][2] * pesanan[i][3] * harga[0]
                            else:
                                pesanan[i][5] = pesanan[i][2] * pesanan[i][3] * harga[1]

                elif menu == "4":
                    if len(pesanan) == 0:
                        print("Belum ada pesanan")
                    else:
                        for i in range(len(pesanan)):
                            print(i + 1, pesanan[i][0], pesanan[i][1], pesanan[i][6])
                        no = input("Nomor pesanan yang mau dihapus: ")

                        i = -1
                        for n in range(len(pesanan)):
                            if no == str(n + 1):
                                i = n

                        if i == -1:
                            print("Nomor tidak ada!")
                        else:
                            yakin = input("Yakin mau dihapus? (y/n): ")
                            if yakin == "y":
                                del pesanan[i]
                                print("Data berhasil dihapus")
                            else:
                                print("Batal dihapus")

                elif menu == "5":
                    print("Logout berhasil")
                    break

                else:
                    print("Menu tidak ada!")

        else:
            print("Login berhasil, halo", user)
            while True:
                print()
                print("=== MENU PENGGUNA ===")
                print("1. Buat pesanan")
                print("2. Lihat pesanan saya")
                print("3. Logout")
                menu = input("Pilih menu: ")

                if menu == "1":
                    print("Nama pemesan:", user)
                    dok = input("Jenis dokumen: ")
                    hal = input("Jumlah halaman: ")
                    rkp = input("Jumlah rangkap: ")
                    print("1. Hitam Putih (Rp1000 per lembar)")
                    print("2. Warna (Rp2000 per lembar)")
                    jns = input("Pilih jenis cetak: ")

                    benar = True
                    for c in hal + rkp:
                        cocok = False
                        for d in angka:
                            if c == d:
                                cocok = True
                        if cocok == False:
                            benar = False
                    if hal == "" or rkp == "":
                        benar = False

                    if dok == "":
                        print("Jenis dokumen tidak boleh kosong!")
                    elif benar == False:
                        print("Halaman dan rangkap harus angka!")
                    elif int(hal) == 0 or int(rkp) == 0:
                        print("Halaman dan rangkap minimal 1!")
                    elif jns != "1" and jns != "2":
                        print("Pilihan jenis cetak salah!")
                    else:
                        total = int(hal) * int(rkp) * harga[int(jns) - 1]
                        pesanan.append([user, dok, int(hal), int(rkp), jenis[int(jns) - 1], total, "Diproses"])
                        print("Pesanan berhasil dibuat")
                        print("Total biaya: Rp", total)

                elif menu == "2":
                    no = 1
                    for p in pesanan:
                        if p[0] == user:
                            print("No:", no)
                            print("Dokumen:", p[1])
                            print("Halaman:", p[2])
                            print("Rangkap:", p[3])
                            print("Jenis cetak:", p[4])
                            print("Total biaya: Rp", p[5])
                            print("Status:", p[6])
                            print()
                            no += 1
                    if no == 1:
                        print("Kamu belum punya pesanan")

                elif menu == "3":
                    print("Logout berhasil")
                    break

                else:
                    print("Menu tidak ada!")

    elif pilih == "2":
        u = input("Username baru: ")
        ada = False
        for a in akun:
            if a[0] == u:
                ada = True

        if u == "":
            print("Username tidak boleh kosong!")
        elif ada == True:
            print("Username sudah dipakai!")
        else:
            pw = input("Password baru: ")
            if len(pw) < 4:
                print("Password minimal 4 karakter!")
            else:
                akun.append([u, pw, "user"])
                print("Register berhasil, silakan login")

    elif pilih == "3":
        print("Terima kasih")
        break

    else:
        print("Menu tidak ada")