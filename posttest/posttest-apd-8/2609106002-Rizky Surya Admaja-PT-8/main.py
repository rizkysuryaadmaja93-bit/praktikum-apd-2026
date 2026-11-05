from autentikasi import login, register
from utilitas import bersihkan_layar, pilih_menu
from tampilan import tampilkan_judul


def tampilkan_menu():
    bersihkan_layar()
    tampilkan_judul("PENGHITUNG BIAYA CETAK DOKUMEN")
    menu = pilih_menu("Pilih menu", ["Login", "Register", "Keluar"])

    if menu == "Login":
        login()
    elif menu == "Register":
        register()
    elif menu == "Keluar":
        print("Terima kasih")
        exit()


if __name__ == "__main__":
    while True:
        tampilkan_menu()