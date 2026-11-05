# menu.py
# menu untuk admin dan pengguna

from pesanan_crud import tambah_pesanan, edit_pesanan, hapus_pesanan
from utilitas import pilih_menu
from tampilan import (tampilkan_judul, tampilkan_semua_pesanan,
                      tampilkan_pesanan_user, cetak_sukses)


def menu_admin(user):
    while True:
        print()
        tampilkan_judul("MENU ADMIN")
        menu = pilih_menu("Pilih menu", ["Tambah pesanan", "Lihat pesanan", "Ubah pesanan", "Hapus pesanan", "Logout"])

        if menu == "Tambah pesanan":
            nama = input("Nama pemesan: ")
            tambah_pesanan(nama)
        elif menu == "Lihat pesanan":
            tampilkan_semua_pesanan()
        elif menu == "Ubah pesanan":
            edit_pesanan()
        elif menu == "Hapus pesanan":
            hapus_pesanan()
        elif menu == "Logout":
            cetak_sukses("Logout berhasil")
            break


def menu_pengguna(user):
    while True:
        print()
        tampilkan_judul("MENU PENGGUNA")
        menu = pilih_menu("Pilih menu", ["Buat pesanan", "Lihat pesanan saya", "Logout"])

        if menu == "Buat pesanan":
            print("Nama pemesan:", user)
            tambah_pesanan(user)
        elif menu == "Lihat pesanan saya":
            tampilkan_pesanan_user(user)
        elif menu == "Logout":
            cetak_sukses("Logout berhasil")
            break