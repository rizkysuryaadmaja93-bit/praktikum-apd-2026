# tampilan.py
# semua output program (tabel prettytable dan warna colorama)

from prettytable import PrettyTable
from colorama import Fore, Style, init
from data import pesanan
from utilitas import format_rupiah, jumlah_pendapatan

init(autoreset=True)


def cetak_sukses(teks):
    print(Fore.GREEN + str(teks))


def cetak_error(teks):
    print(Fore.RED + str(teks))


def warna_status(status):
    if status == "Selesai":
        return Fore.GREEN + status + Style.RESET_ALL
    else:
        return Fore.YELLOW + status + Style.RESET_ALL


def tampilkan_judul(teks):
    tabel = PrettyTable()
    tabel.header = False
    tabel.add_row([teks])
    print(tabel)


def tampilkan_semua_pesanan():
    tabel = PrettyTable()
    tabel.title = "DAFTAR SEMUA PESANAN"
    tabel.field_names = ["ID", "Pemesan", "Dokumen", "Halaman", "Rangkap", "Jenis", "Total", "Status", "Tanggal"]
    tabel.align["Total"] = "r"
    selesai = 0
    semua_total = []
    for i, j in pesanan.items():
        tabel.add_row([i, j["nama"], j["dokumen"], j["halaman"], j["rangkap"], j["jenis"], format_rupiah(j["total"]), warna_status(j["status"]), j["tanggal"]])
        semua_total.append(j["total"])
        if j["status"] == "Selesai":
            selesai += 1
    print(tabel)

    # tabel rekap
    rekap = PrettyTable()
    rekap.title = "REKAP PESANAN"
    rekap.field_names = ["Keterangan", "Nilai"]
    rekap.align["Keterangan"] = "l"
    rekap.align["Nilai"] = "r"
    rekap.add_row(["Jumlah pesanan", len(pesanan)])
    rekap.add_row(["Sudah selesai", selesai])
    rekap.add_row(["Masih diproses", len(pesanan) - selesai])
    rekap.add_row(["Pesanan termahal", format_rupiah(max(semua_total))])
    rekap.add_row(["Rata-rata pesanan", format_rupiah(round(sum(semua_total) / len(semua_total)))])
    rekap.add_row(["Total pendapatan", format_rupiah(jumlah_pendapatan(list(pesanan.keys()), 0))])
    print(rekap)


def tampilkan_pesanan_user(user):
    tabel = PrettyTable()
    tabel.title = "PESANAN SAYA"
    tabel.field_names = ["ID", "Dokumen", "Halaman", "Rangkap", "Jenis", "Total", "Status", "Tanggal"]
    tabel.align["Total"] = "r"
    pengeluaran = 0
    ada = False
    for i, j in pesanan.items():
        if j["nama"] == user:
            tabel.add_row([i, j["dokumen"], j["halaman"], j["rangkap"], j["jenis"], format_rupiah(j["total"]), warna_status(j["status"]), j["tanggal"]])
            pengeluaran += j["total"]
            ada = True
    if ada == False:
        cetak_error("Kamu belum punya pesanan")
    else:
        tabel.add_row(["", "", "", "", "TOTAL", format_rupiah(pengeluaran), "", ""])
        print(tabel)


def cetak_struk(nomor):
    data = pesanan[nomor]
    tabel = PrettyTable()
    tabel.title = "STRUK CETAK"
    tabel.header = False
    tabel.align = "l"
    tabel.add_row(["ID Pesanan", nomor])
    tabel.add_row(["Kode", data["kode"]])
    tabel.add_row(["Pemesan", data["nama"]])
    tabel.add_row(["Dokumen", data["dokumen"]])
    tabel.add_row(["Halaman", data["halaman"]])
    tabel.add_row(["Rangkap", data["rangkap"]])
    tabel.add_row(["Jenis", data["jenis"]])
    tabel.add_row(["Status", warna_status(data["status"])])
    tabel.add_row(["Tanggal", data["tanggal"]])
    tabel.add_row(["TOTAL", format_rupiah(data["total"])])
    print(tabel)