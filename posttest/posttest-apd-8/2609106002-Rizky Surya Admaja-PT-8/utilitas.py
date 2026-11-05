# utilitas.py
# fungsi-fungsi bantu yang dipakai di file lain

import os
import random
import inquirer
from datetime import datetime
from data import pesanan, id_terakhir, harga


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def tanggal_hari_ini():
    # format tgl/bln/thn
    return datetime.now().strftime("%d/%m/%Y")


def buat_kode_pesanan():
    # kode acak 4 angka, contoh CTK-8392
    angka = "0123456789"
    kode = ""
    for i in range(4):
        kode += random.choice(angka)
    return "CTK-" + kode


def buat_id_baru():
    id_terakhir[0] += 1
    id_baru = id_terakhir[0]
    return id_baru


def pilih_menu(pesan, daftar):
    # menu pilihan pakai panah keyboard (inquirer)
    pertanyaan = [
        inquirer.List("pilihan", message=pesan, choices=daftar),
    ]
    jawaban = inquirer.prompt(pertanyaan)
    if jawaban is None:
        # kalau user tekan Ctrl+C
        print("Program dihentikan")
        exit()
    return jawaban["pilihan"]


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
    # rekursif, hitung total pesanan yang sudah selesai
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


def pilih_jenis_cetak():
    pilihan = pilih_menu("Pilih jenis cetak", ["Hitam Putih (Rp1.000 per lembar)", "Warna (Rp2.000 per lembar)"])
    # ambil nama jenisnya saja (sebelum tanda kurung)
    return pilihan.split(" (")[0]


# bagian ini cuma jalan kalau utilitas.py dijalankan langsung
if __name__ == "__main__":
    print("Tes format_rupiah:", format_rupiah(1500000))
    print("Tes hitung_total:", hitung_total(10, 2, "Warna"))
    print("Tes kode pesanan:", buat_kode_pesanan())
    print("Tes tanggal:", tanggal_hari_ini())