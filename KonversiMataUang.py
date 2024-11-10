RESET = "\033[0m"    
HIJAU = "\033[92m"     
MERAH = "\033[91m"   

def konversi_mata_uang(mata_uang_asal, mata_uang_tujuan, jumlah):
    if mata_uang_asal == "IDR" and mata_uang_tujuan == "USD":
        return jumlah * 0.000065 
    elif mata_uang_asal == "IDR" and mata_uang_tujuan == "EUR":
        return jumlah * 0.000058 
    elif mata_uang_asal == "USD" and mata_uang_tujuan == "IDR":
        return jumlah * 15385  
    elif mata_uang_asal == "USD" and mata_uang_tujuan == "EUR":
        return jumlah * 0.89  
    elif mata_uang_asal == "EUR" and mata_uang_tujuan == "IDR":
        return jumlah * 17241
    elif mata_uang_asal == "EUR" and mata_uang_tujuan == "USD":
        return jumlah * 1.13 
    else:
        print(f"{MERAH}Konversi mata uang tidak didukung.{RESET}")
        return None

def get_input_mata_uang():
    while True:
        mata_uang_asal = input("Masukkan mata uang asal (IDR, USD, EUR): ").upper()
        mata_uang_tujuan = input("Masukkan mata uang tujuan (IDR, USD, EUR): ").upper()
        
        if mata_uang_asal not in ["IDR", "USD", "EUR"] or mata_uang_tujuan not in ["IDR", "USD", "EUR"]:
            print(f"{MERAH}Mata uang tidak valid. Silakan masukkan IDR, USD, atau EUR.{RESET}")
        else:
            break 

    while True:
        try:
            jumlah = float(input("Masukkan jumlah uang yang akan dikonversi: "))
            if jumlah <= 0:
                print(f"{MERAH}Jumlah harus angka positif.{RESET}")
            else:
                break 
        except ValueError:
            print(f"{MERAH}Jumlah tidak valid. Masukkan angka.{RESET}")
    
    return mata_uang_asal, mata_uang_tujuan, jumlah

mata_uang_asal, mata_uang_tujuan, jumlah = get_input_mata_uang()

if mata_uang_asal and mata_uang_tujuan and jumlah:
    hasil = konversi_mata_uang(mata_uang_asal, mata_uang_tujuan, jumlah)
    if hasil is not None:
        print(f"{HIJAU}{jumlah} {mata_uang_asal} = {hasil:.2f} {mata_uang_tujuan}{RESET}")
