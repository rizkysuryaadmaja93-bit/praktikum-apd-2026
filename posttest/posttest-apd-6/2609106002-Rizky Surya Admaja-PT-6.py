import os
akun = {
    "admin1": {"password": "admin123", "role": "admin"},
    "admin2": {"password": "admin456", "role": "admin"},
    "surya": {"password": "surya123", "role": "user"},
    "rizky": {"password": "rizky456", "role": "user"}
}

pesanan = {
    1: {"nama": "surya", "dokumen": "Skripsi", "halaman": 100, "rangkap": 1, "jenis": "Hitam Putih", "total": 100000, "status": "Diproses"},
    2: {"nama": "rizky", "dokumen": "Poster", "halaman": 5, "rangkap": 1, "jenis": "Warna", "total": 10000, "status": "Selesai"}
}
id_baru = 2

jenis = {"1": "Hitam Putih", "2": "Warna"}
harga = {"Hitam Putih": 1000, "Warna": 2000}
angka = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("===========================================")
    print("      PENGHITUNG BIAYA CETAK DOKUMEN    ")
    print("===========================================")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    print("===========================================")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        user = input("Username: ")
        pw = input("Password: ")

        if akun.get(user) == None:
            print("Username atau password salah!")
        elif akun[user]["password"] != pw:
            print("Username atau password salah!")

        elif akun[user]["role"] == "admin":
            print("Login berhasil, halo admin", user)
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
                    for i in hal + rkp:
                        cocok = False
                        for j in angka:
                            if i == j:
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
                    elif jenis.get(jns) == None:
                        print("Pilihan jenis cetak salah!")
                    else:
                        total = int(hal) * int(rkp) * harga[jenis[jns]]
                        id_baru += 1
                        pesanan.update({id_baru: {"nama": nama, "dokumen": dok, "halaman": int(hal), "rangkap": int(rkp), "jenis": jenis[jns], "total": total, "status": "Diproses"}})
                        print("Pesanan berhasil ditambahkan")
                        print("Total biaya: Rp", total)

                elif menu == "2":
                    if len(pesanan) == 0:
                        print("Belum ada pesanan")
                    else:
                        pendapatan = 0
                        for i, j in pesanan.items():
                            print("ID Pesanan:", i)
                            for k, v in j.items():
                                print(f"{k} : {v}")
                            print()
                            if j["status"] == "Selesai":
                                pendapatan = pendapatan + j["total"]
                        print("Jumlah pesanan:", len(pesanan))
                        print("Total pendapatan: Rp", pendapatan)

                elif menu == "3":
                    if len(pesanan) == 0:
                        print("Belum ada pesanan")
                    else:
                        for i, j in pesanan.items():
                            print(i, j["nama"], j["dokumen"], j["status"])
                        no = input("ID pesanan yang mau diubah: ")

                        benar = True
                        for i in no:
                            cocok = False
                            for j in angka:
                                if i == j:
                                    cocok = True
                            if cocok == False:
                                benar = False
                        if no == "":
                            benar = False

                        if benar == False:
                            print("ID harus angka!")
                        elif pesanan.get(int(no)) == None:
                            print("ID tidak ada!")
                        else:
                            id = int(no)
                            print("1. Jumlah halaman")
                            print("2. Jumlah rangkap")
                            print("3. Jenis cetak")
                            print("4. Status")
                            ubah = input("Mau ubah yang mana: ")

                            if ubah == "1":
                                baru = input("Halaman baru: ")
                                benar = True
                                for i in baru:
                                    cocok = False
                                    for j in angka:
                                        if i == j:
                                            cocok = True
                                    if cocok == False:
                                        benar = False
                                if baru == "" or benar == False:
                                    print("Input harus angka!")
                                elif int(baru) == 0:
                                    print("Input minimal 1!")
                                else:
                                    pesanan[id]["halaman"] = int(baru)
                                    print("Data berhasil diubah")
                            elif ubah == "2":
                                baru = input("Rangkap baru: ")
                                benar = True
                                for i in baru:
                                    cocok = False
                                    for j in angka:
                                        if i == j:
                                            cocok = True
                                    if cocok == False:
                                        benar = False
                                if baru == "" or benar == False:
                                    print("Input harus angka!")
                                elif int(baru) == 0:
                                    print("Input minimal 1!")
                                else:
                                    pesanan[id]["rangkap"] = int(baru)
                                    print("Data berhasil diubah")
                            elif ubah == "3":
                                print("1. Hitam Putih")
                                print("2. Warna")
                                baru = input("Pilih: ")
                                if jenis.get(baru) != None:
                                    pesanan[id].update({"jenis": jenis[baru]})
                                    print("Data berhasil diubah")
                                else:
                                    print("Pilihan salah!")
                            elif ubah == "4":
                                print("1. Diproses")
                                print("2. Selesai")
                                baru = input("Pilih: ")
                                if baru == "1":
                                    pesanan[id].update({"status": "Diproses"})
                                    print("Data berhasil diubah")
                                elif baru == "2":
                                    pesanan[id].update({"status": "Selesai"})
                                    print("Data berhasil diubah")
                                else:
                                    print("Pilihan salah!")
                            else:
                                print("Pilihan salah!")

                            pesanan[id]["total"] = pesanan[id]["halaman"] * pesanan[id]["rangkap"] * harga[pesanan[id]["jenis"]]

                elif menu == "4":
                    if len(pesanan) == 0:
                        print("Belum ada pesanan")
                    else:
                        for i, j in pesanan.items():
                            print(i, j["nama"], j["dokumen"], j["status"])
                        no = input("ID pesanan yang mau dihapus: ")

                        benar = True
                        for i in no:
                            cocok = False
                            for j in angka:
                                if i == j:
                                    cocok = True
                            if cocok == False:
                                benar = False
                        if no == "":
                            benar = False

                        if benar == False:
                            print("ID harus angka!")
                        elif pesanan.get(int(no)) == None:
                            print("ID tidak ada!")
                        else:
                            yakin = input("Yakin mau dihapus? (ya/tidak): ")
                            if yakin == "ya":
                                cache = pesanan.pop(int(no))
                                print("Pesanan atas nama", cache["nama"], "berhasil dihapus")
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
                    for i in hal + rkp:
                        cocok = False
                        for j in angka:
                            if i == j:
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
                    elif jenis.get(jns) == None:
                        print("Pilihan jenis cetak salah!")
                    else:
                        total = int(hal) * int(rkp) * harga[jenis[jns]]
                        id_baru += 1
                        pesanan.update({id_baru: {"nama": user, "dokumen": dok, "halaman": int(hal), "rangkap": int(rkp), "jenis": jenis[jns], "total": total, "status": "Diproses"}})
                        print("Pesanan berhasil dibuat")
                        print("Total biaya: Rp", total)

                elif menu == "2":
                    ada = False
                    for i, j in pesanan.items():
                        if j["nama"] == user:
                            print("ID Pesanan:", i)
                            print("Dokumen:", j["dokumen"])
                            print("Halaman:", j["halaman"])
                            print("Rangkap:", j["rangkap"])
                            print("Jenis cetak:", j["jenis"])
                            print("Total biaya: Rp", j["total"])
                            print("Status:", j["status"])
                            print()
                            ada = True
                    if ada == False:
                        print("Kamu belum punya pesanan")

                elif menu == "3":
                    print("Logout berhasil")
                    break

                else:
                    print("Menu tidak ada!")

    elif pilih == "2":
        u = input("Username baru: ")

        if u == "":
            print("Username tidak boleh kosong!")
        elif akun.get(u) != None:
            print("Username sudah dipakai!")
        else:
            pw = input("Password baru: ")
            if len(pw) < 4:
                print("Password minimal 4 karakter!")
            else:
                akun[u] = {"password": pw, "role": "user"}
                print("Register berhasil, silakan login")

    elif pilih == "3":
        print("Terima kasih")
        break

    else:
        print("Menu tidak ada")