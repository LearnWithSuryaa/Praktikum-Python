import time
RESET = "\033[0m"    
HIJAU = "\033[92m"     
MERAH = "\033[91m"   

def get_waktu_alarm():
    while True:
        try:
            waktu_alarm = int(input("Masukkan waktu alarm dalam detik (harus angka positif): "))
            if waktu_alarm > 0:
                return waktu_alarm
            else:
                print(f"{MERAH}Masukkan angka positif lebih dari 0.{RESET}")
                
        except ValueError:
            print(f"{MERAH}Input tidak valid. Harap masukkan angka.{RESET}")
            
waktu_alarm = get_waktu_alarm()

print(f"{HIJAU}Alarm disetel...{RESET}")

time.sleep(waktu_alarm)

print(f"{MERAH}Waktu habis! Alarm berbunyi!{RESET}")
print("\a")
