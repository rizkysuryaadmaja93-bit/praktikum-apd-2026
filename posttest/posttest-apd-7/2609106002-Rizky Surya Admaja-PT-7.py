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
 
id_terakhir = [2]
 
jenis = {"1": "Hitam Putih", "2": "Warna"}
harga = {"Hitam Putih": 1000, "Warna": 2000}
 
 
def buat_id_baru():
    id_terakhir[0] += 1
    id_baru = id_terakhir[0]
    return id_baru
 
 
def pilih_jenis_cetak():
    print("[1] Hitam Putih (Rp1.000 per lembar)")
    print("[2] Warna (Rp2.000 per lembar)")
    pilihan = input("Pilih jenis cetak: ")
    if pilihan not in jenis:
        raise ValueError("Pilihan jenis cetak tidak valid")
    return jenis[pilihan]
 
 
def input_angka(teks):
    try:
        angka = int(input(teks))
    except ValueError:
        raise ValueError("Input yang anda masukkan bukan Integer (angka)")
    if angka < 1:
        raise ValueError("Input minimal 1")
    return angka
 
 
def hitung_total(halaman, rangkap, jenis_cetak):
    total = halaman * rangkap * harga[jenis_cetak]
    return total
 
 
def format_rupiah(angka):
    teks = f"{angka:,}"
    teks = teks.replace(",", ".")
    return "Rp" + teks
 
 
def jumlah_pendapatan(daftar_id, index):
    if index == len(daftar_id):
        return 0
    else:
        data = pesanan[daftar_id[index]]
        if data["status"] == "Selesai":
            return data["total"] + jumlah_pendapatan(daftar_id, index + 1)
        else:
            return jumlah_pendapatan(daftar_id, index + 1)
 
 
def cek_password(pw):
    if len(pw) < 10:
        raise ValueError("Password minimal memiliki 10 karakter")
    if pw[0].isupper() == False:
        raise ValueError("Huruf awal password wajib kapital")
    ada_angka = False
    for huruf in pw:
        if huruf.isdigit():
            ada_angka = True
    if ada_angka == False:
        raise ValueError("Password wajib mengandung angka")
 
 
def cetak_struk(nomor):
    data = pesanan[nomor]
    print("==============================")
    print("         STRUK CETAK          ")
    print("==============================")
    print(f"ID Pesanan : {nomor}")
    print(f"Pemesan    : {data['nama']}")
    print(f"Dokumen    : {data['dokumen']}")
    print(f"Halaman    : {data['halaman']}")
    print(f"Rangkap    : {data['rangkap']}")
    print(f"Jenis      : {data['jenis']}")
    print(f"Status     : {data['status']}")
    print("------------------------------")
    print(f"TOTAL      : {format_rupiah(data['total'])}")
    print("==============================")
 
 
def lihat_pesanan():
    if len(pesanan) <= 0:
        print("Belum ada data pesanan")
    else:
        selesai = 0
        for i, j in pesanan.items():
            print(f"ID Pesanan : {i}")
            print(f"Pemesan    : {j['nama']}")
            print(f"Dokumen    : {j['dokumen']} ({j['halaman']} hal x {j['rangkap']} rangkap)")
            print(f"Jenis      : {j['jenis']}")
            print(f"Total      : {format_rupiah(j['total'])}")
            print(f"Status     : {j['status']}")
            print("------------------------------")
            if j["status"] == "Selesai":
                selesai += 1
        print("Jumlah pesanan   :", len(pesanan))
        print("Sudah selesai    :", selesai)
        print("Masih diproses   :", len(pesanan) - selesai)
        print("Total pendapatan :", format_rupiah(jumlah_pendapatan(list(pesanan.keys()), 0)))
 
 
def lihat_pesanan_saya(user):
    ada = False
    pengeluaran = 0
    for i, j in pesanan.items():
        if j["nama"] == user:
            print(f"ID Pesanan : {i}")
            print(f"Dokumen    : {j['dokumen']} ({j['halaman']} hal x {j['rangkap']} rangkap)")
            print(f"Jenis      : {j['jenis']}")
            print(f"Total      : {format_rupiah(j['total'])}")
            print(f"Status     : {j['status']}")
            print("------------------------------")
            pengeluaran += j["total"]
            ada = True
    if ada == False:
        print("Kamu belum punya pesanan")
    else:
        print("Total semua pesanan kamu:", format_rupiah(pengeluaran))
 
 
def tambah_pesanan(nama):
    try:
        if nama == "":
            raise ValueError("Nama pemesan tidak boleh kosong")
        dok = input("Jenis dokumen: ")
        if dok == "":
            raise ValueError("Jenis dokumen tidak boleh kosong")
        hal = input_angka("Jumlah halaman: ")
        rkp = input_angka("Jumlah rangkap: ")
        jns = pilih_jenis_cetak()
    except ValueError as e:
        print(e)
    else:
        total = hitung_total(hal, rkp, jns)
        nomor = buat_id_baru()
        pesanan.update({nomor: {"nama": nama, "dokumen": dok, "halaman": hal, "rangkap": rkp, "jenis": jns, "total": total, "status": "Diproses"}})
        print("Pesanan berhasil ditambahkan!")
        cetak_struk(nomor)
    finally:
        print("Blok Try Selesai")
 
 
def edit_pesanan():
    if len(pesanan) <= 0:
        print("Belum ada data pesanan")
    else:
        lihat_pesanan()
        try:
            no = input_angka("Masukkan ID Pesanan: ")
            data = pesanan[no]
            print("[1] Jumlah Halaman")
            print("[2] Jumlah Rangkap")
            print("[3] Jenis Cetak")
            print("[4] Status")
            ubah = input("Mau ubah yang mana: ")
            if ubah == "1":
                data["halaman"] = input_angka("Halaman baru: ")
            elif ubah == "2":
                data["rangkap"] = input_angka("Rangkap baru: ")
            elif ubah == "3":
                data["jenis"] = pilih_jenis_cetak()
            elif ubah == "4":
                print("[1] Diproses")
                print("[2] Selesai")
                baru = input("Pilih status: ")
                if baru == "1":
                    data["status"] = "Diproses"
                elif baru == "2":
                    data["status"] = "Selesai"
                else:
                    raise ValueError("Pilihan status tidak valid")
            else:
                raise ValueError("Pilihan tidak valid")
        except ValueError as e:
            print(e)
        except KeyError:
            print("ID tidak valid")
        else:
            data["total"] = hitung_total(data["halaman"], data["rangkap"], data["jenis"])
            print("Pesanan berhasil diupdate!")
 
 
def hapus_pesanan():
    if len(pesanan) <= 0:
        print("Belum ada data pesanan")
    else:
        lihat_pesanan()
        try:
            no = input_angka("Masukkan ID Pesanan: ")
            data = pesanan[no]
        except ValueError as e:
            print(e)
        except KeyError:
            print("ID tidak valid")
        else:
            yakin = input("Yakin mau dihapus? (ya/tidak): ")
            if yakin == "ya":
                pesanan.pop(no)
                print("Pesanan atas nama", data["nama"], "berhasil dihapus!")
            else:
                print("Batal dihapus")
 
 
def menu_admin(user):
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
            tambah_pesanan(nama)
        elif menu == "2":
            lihat_pesanan()
        elif menu == "3":
            edit_pesanan()
        elif menu == "4":
            hapus_pesanan()
        elif menu == "5":
            print("Logout berhasil")
            break
        else:
            print("Menu tidak ada!")
 
 
def menu_pengguna(user):
    while True:
        print()
        print("=== MENU PENGGUNA ===")
        print("1. Buat pesanan")
        print("2. Lihat pesanan saya")
        print("3. Logout")
        menu = input("Pilih menu: ")
 
        if menu == "1":
            print("Nama pemesan:", user)
            tambah_pesanan(user)
        elif menu == "2":
            lihat_pesanan_saya(user)
        elif menu == "3":
            print("Logout berhasil")
            break
        else:
            print("Menu tidak ada!")
 
 
def login():
    user = input("Username: ")
    pw = input("Password: ")
    try:
        if akun[user]["password"] != pw:
            raise ValueError("Username atau password salah")
    except KeyError:
        print("Username atau password salah")
        input("Tekan Enter untuk lanjut...")
    except ValueError as e:
        print(e)
        input("Tekan Enter untuk lanjut...")
    else:
        if akun[user]["role"] == "admin":
            print("Login berhasil, halo admin", user)
            menu_admin(user)
        else:
            print("Login berhasil, halo", user)
            menu_pengguna(user)
 
 
def register():
    u = input("Username baru: ")
    pw = input("Password baru: ")
    try:
        if u == "":
            raise ValueError("Username tidak boleh kosong")
        if u in akun:
            raise ValueError("Username sudah dipakai")
        cek_password(pw)
    except ValueError as e:
        print(e)
    else:
        akun[u] = {"password": pw, "role": "user"}
        print("Register berhasil, silakan login")
    finally:
        print("Blok Try Selesai")
        input("Tekan Enter untuk lanjut...")
 
 
def tampilkan_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print("===========================================")
    print("      PENGHITUNG BIAYA CETAK DOKUMEN    ")
    print("===========================================")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    print("===========================================")
    menu = input("Pilih menu: ")
 
    if menu == "1":
        login()
    elif menu == "2":
        register()
    elif menu == "3":
        print("Terima kasih")
        exit()
    else:
        print("Menu tidak ada")
        input("Tekan Enter untuk lanjut...")
 
 
if __name__ == "__main__":
    while(True):
        tampilkan_menu()
 