RESET = "\033[0m"    
HIJAU = "\033[92m"     
MERAH = "\033[91m"    
BIRU = "\033[94m" 

daftar = []

print("=== Aplikasi Daftar Tugas ===")
print("Panduan penggunaan:")
print("1. Ketik 'tambah' untuk menambah tugas")
print("2. Ketik 'hapus' untuk menghapus tugas")
print("3. Ketik 'tampilkan' untuk melihat daftar tugas")
print("4. Ketik 'keluar' untuk keluar dari aplikasi")

while True:
    pilihan = input("\nApa yang ingin Anda lakukan? ").strip().lower()

    if pilihan == "tambah":
        tugas = input("Masukkan tugas baru: ").strip()
        if tugas: 
            daftar.append(tugas)
            print(f"{HIJAU}Tugas '{tugas}' telah ditambahkan.{RESET}")
        else:
            print(f"{MERAH}Tugas tidak boleh kosong!{RESET}")

    elif pilihan == "hapus":
        if len(daftar) == 0:  
            print(f"{MERAH}Daftar tugas kosong, tidak ada yang bisa dihapus.{RESET}")
        else:
            print("Daftar tugas saat ini:")
            for i, tugas in enumerate(daftar, start=1):
                print(f"{i}. {tugas}")
            try:
                nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
                if 1 <= nomor <= len(daftar):
                    tugas_dihapus = daftar.pop(nomor - 1)
                    print(f"{HIJAU}Tugas '{tugas_dihapus}' telah dihapus.{RESET}")
                else:
                    print(f"{MERAH}Nomor tidak valid.{RESET}")
            except ValueError:
                print(f"{MERAH}Harap masukkan angka yang benar.{RESET}")

    elif pilihan == "tampilkan":
        if len(daftar) == 0:
            print(f"{MERAH}Daftar tugas kosong.{RESET}")
        else:
            print("Daftar tugas saat ini:")
            for i, tugas in enumerate(daftar, start=1):
                print(f"{i}. {tugas}")

    elif pilihan == "keluar":
        print(f"{HIJAU}Terima kasih telah menggunakan aplikasi daftar tugas!{RESET}")
        break

    else:
        print(f"{MERAH}Pilihan tidak dikenali. Silakan coba lagi.{RESET}")
