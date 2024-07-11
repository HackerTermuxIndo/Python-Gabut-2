import time
import os
import colorama
from colorama import Fore, Style, Back
os.system('clear')
print(Style.BRIGHT, Fore.CYAN)
os.system('figlet gabut')
print(Style.BRIGHT, Fore.YELLOW)

while True:
    print(Style.BRIGHT, Back.RED, Fore.WHITE + "SEDANG MENUNGGU PERINTAH 😁" + Style.RESET_ALL)
    print()
    print(Style.BRIGHT, Fore.YELLOW + "1. Ngepet pulsa")
    print(Style.BRIGHT, Fore.YELLOW + "2. Hack Satelit Nasa")
    print(Fore.BLUE + " 3. Kirim virtex")
    print(Style.BRIGHT, Fore.BLUE + "4. Hack No WA")
    print(Style.BRIGHT, Fore.RED + "5. Exit")
    print()
    prank_choice = int(input(Fore.YELLOW + "Pilih nomor berapa : "))
    
    if prank_choice == 1:
        os.system('clear')
        os.system('figlet Ngepet')
        print()
        input_nomor = input('Masukkan nomor/huruf target : ')
        input_jumlah = int(input('Mau ngepet berapa kali : '))

        for _ in range(input_jumlah):
            print(Fore.RED + f"Berhasil ngepet nomor {input_nomor} sebanyak {input_jumlah} Kali")
            time.sleep(0.05)
        
        break  # Berhenti setelah perintah pertama selesai
        
    elif prank_choice == 2:
        os.system('clear')
        os.system('figlet Satelit')
        input_satelit = input('Masukkan nama satelit : ')
        time.sleep(1)
        print(Fore.CYAN + "Tunggu...")
        time.sleep(5)
        time.sleep(3)
        print(Fore.GREEN + f"Berhasil merubah arah satelit {input_satelit} ke 30° LT ")
        print(Fore.RED + f"Satelit dengan nama {input_satelit} telah Tergeser ⚠️")
        break  # kode berhenti setelah perintah pertama selesai
        
    elif prank_choice == 3:
        os.system('clear')
        os.system('figlet virtex')
        print()
        input_nomor = input('Masukkan nomor telp target : ')
        input_jumlah_vir = int(input('Mau ngirim vir brp kali : '))

        for _ in range(input_jumlah_vir):
            print(Fore.CYAN + f"Berhasil ngepet nomor {input_nomor} sebanyak {input_jumlah_vir} Kali")
            time.sleep(0.02)
        
        break
        
    elif prank_choice == 4:
        os.system('clear')
        os.system('figlet HackWA')
        input_nohp = input('Masukkan no hp : ')
        input_ganti = int(input('mau ganti no hp ini dengan no apa : '))
        time.sleep(1)
        print(Fore.CYAN + "Wait... 😁")
        time.sleep(5)
        time.sleep(3)
        print(Fore.GREEN + f"Berhasil Merubah no telp {input_nohp} menjadi {input_ganti}")
        print(Fore.RED + f"no telp {input_nohp} telah terganti ⚠️")
        break  # kode berhenti setelah perintah pertama selesai
        
    elif prank_choice == 5:
        print("bye")
        break

    else:
        print(Fore.RED + "Pilihan tidak valid.")
