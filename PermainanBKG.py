RESET = "\033[0m"    
HIJAU = "\033[92m"     
MERAH = "\033[91m"  
BIRU = "\033[94m" 

import random

pilihan = ["batu", "kertas", "gunting"]

def tentukan_pemenang(pilihan_user, pilihan_kom):
    if pilihan_user == pilihan_kom:
        return f"{BIRU}Seri{RESET}"
    elif (pilihan_user == "batu" and pilihan_kom == "gunting") or \
         (pilihan_user == "kertas" and pilihan_kom == "batu") or \
         (pilihan_user == "gunting" and pilihan_kom == "kertas"):
        return f"{HIJAU}Anda menang!{RESET}"
    else:
        return f"{MERAH}Komputer menang!{RESET}"

print("Selamat datang di permainan Batu, Kertas, Gunting!")
while True:
    pilihan_user = input("Pilih batu, kertas, atau gunting (ketik 'keluar' untuk berhenti): ").lower()

    if pilihan_user == 'keluar':
        print(f"{HIJAU}Terima kasih telah bermain!{RESET}")
        break

    if pilihan_user not in pilihan:
        print(f"{MERAH}Input tidak valid! Harap pilih antara batu, kertas, atau gunting.{RESET}")
        continue

    pilihan_kom = random.choice(pilihan)

    print(f"Komputer memilih: {pilihan_kom}")

    hasil = tentukan_pemenang(pilihan_user, pilihan_kom)
    print(hasil)
