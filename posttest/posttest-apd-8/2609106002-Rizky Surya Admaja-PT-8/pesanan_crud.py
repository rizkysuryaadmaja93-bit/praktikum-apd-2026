# pesanan_crud.py
# fungsi tambah, ubah, hapus pesanan

from data import pesanan
from utilitas import (input_angka, pilih_jenis_cetak, hitung_total, buat_id_baru,
                      buat_kode_pesanan, tanggal_hari_ini, pilih_menu)
from tampilan import (tampilkan_semua_pesanan, cetak_struk, cetak_sukses,
                      cetak_error)


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
        cetak_error(e)
    else:
        total = hitung_total(hal, rkp, jns)
        nomor = buat_id_baru()
        pesanan.update({nomor: {"kode": buat_kode_pesanan(), "nama": nama, "dokumen": dok, "halaman": hal, "rangkap": rkp, "jenis": jns, "total": total, "status": "Diproses", "tanggal": tanggal_hari_ini()}})
        cetak_sukses("Pesanan berhasil ditambahkan!")
        cetak_struk(nomor)
    finally:
        print("Blok Try Selesai")


def edit_pesanan():
    if len(pesanan) <= 0:
        cetak_error("Belum ada data pesanan")
    else:
        tampilkan_semua_pesanan()
        try:
            no = input_angka("Masukkan ID Pesanan: ")
            data = pesanan[no]
            ubah = pilih_menu("Mau ubah yang mana?", ["Jumlah Halaman", "Jumlah Rangkap", "Jenis Cetak", "Status"])
            if ubah == "Jumlah Halaman":
                data["halaman"] = input_angka("Halaman baru: ")
            elif ubah == "Jumlah Rangkap":
                data["rangkap"] = input_angka("Rangkap baru: ")
            elif ubah == "Jenis Cetak":
                data["jenis"] = pilih_jenis_cetak()
            elif ubah == "Status":
                data["status"] = pilih_menu("Pilih status", ["Diproses", "Selesai"])
        except ValueError as e:
            cetak_error(e)
        except KeyError:
            cetak_error("ID tidak valid")
        else:
            data["total"] = hitung_total(data["halaman"], data["rangkap"], data["jenis"])
            cetak_sukses("Pesanan berhasil diupdate!")


def hapus_pesanan():
    if len(pesanan) <= 0:
        cetak_error("Belum ada data pesanan")
    else:
        tampilkan_semua_pesanan()
        try:
            no = input_angka("Masukkan ID Pesanan: ")
            data = pesanan[no]
        except ValueError as e:
            cetak_error(e)
        except KeyError:
            cetak_error("ID tidak valid")
        else:
            yakin = pilih_menu("Yakin mau dihapus?", ["Ya", "Tidak"])
            if yakin == "Ya":
                pesanan.pop(no)
                cetak_sukses("Pesanan atas nama " + data["nama"] + " berhasil dihapus!")
            else:
                print("Batal dihapus")