# autentikasi.py
# login dan register

import pwinput
from data import akun
from utilitas import cek_password
from tampilan import cetak_sukses, cetak_error
from menu import menu_admin, menu_pengguna


def login():
    user = input("Username: ")
    pw = pwinput.pwinput("Password: ", mask="*")
    try:
        if akun[user]["password"] != pw:
            raise ValueError("Username atau password salah")
    except KeyError:
        cetak_error("Username atau password salah")
        input("Tekan Enter untuk lanjut...")
    except ValueError as e:
        cetak_error(e)
        input("Tekan Enter untuk lanjut...")
    else:
        if akun[user]["role"] == "admin":
            cetak_sukses("Login berhasil, halo admin " + user)
            menu_admin(user)
        else:
            cetak_sukses("Login berhasil, halo " + user)
            menu_pengguna(user)


def register():
    u = input("Username baru: ")
    pw = pwinput.pwinput("Password baru: ", mask="*")
    try:
        if u == "":
            raise ValueError("Username tidak boleh kosong")
        if u in akun:
            raise ValueError("Username sudah dipakai")
        cek_password(pw)
    except ValueError as e:
        cetak_error(e)
    else:
        akun[u] = {"password": pw, "role": "user"}
        cetak_sukses("Register berhasil, silakan login")
    finally:
        print("Blok Try Selesai")
        input("Tekan Enter untuk lanjut...")