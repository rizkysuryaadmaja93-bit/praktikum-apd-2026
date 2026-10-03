username = "Surya"
password = "002"
pin = "002002"
saldo = 5000000

status_login = False
 
for i in range(3):
    print("============= LOGIN ============")
    input_username = input("Username: ")
    input_password = input("Password: ")

    if input_username == username:
        if input_password == password:
            status_login = True
            break
        else:
            print("Password anda salah")
    else:
        print("Username anda salah")
 
if status_login == False:
    print("=== Akun anda diblokir ===")
else:
    print("==Login berhasil==")

    pilihan = ""

    while(pilihan != "2"):
        print("=== MENU UTAMA ===")
        print("1. Transfer Uang")
        print("2. Logout")
        pilihan = input("Pilih menu: ")
 
        if pilihan == "1":
            jawab = "y"
 
            while(jawab == "y"):
                print(f"Saldo saat ini: Rp{saldo}")
                penerima = input("Username penerima: ")
                nominal = int(input("Nominal transfer: "))
                while(nominal < 50000 or nominal > 1000000 or nominal > saldo):
                    if nominal < 50000:
                        print("Nominal minimal Rp50.000")
                    elif nominal > 1000000:
                        print("Nominal maksimal Rp1.000.000")
                    else:
                        print("Saldo tidak cukup")
                    nominal = int(input("Nominal transfer: "))
                hitung = 0
                pin_benar = False
                while(hitung < 3 and pin_benar == False):
                    input_pin = input("Masukkan PIN: ")
                    if input_pin == pin:
                        pin_benar = True
                    else:
                        print("PIN salah")
                    hitung += 1
 
                if pin_benar == False:
                    print("Akun anda diblokir")
                    pilihan = "2"
                    break

                saldo -= nominal
                print("=== STRUK TRANSFER ===")
                print("Pengirim :", username)
                print("Penerima :", penerima)
                print(f"Nominal  : Rp{nominal}")
 
                jawab = input("Apakah ingin transfer lagi (y/n)? ")
 
        elif pilihan == "2":
            print("Anda telah logout")
        else:
            print("Pilihan tidak valid")
