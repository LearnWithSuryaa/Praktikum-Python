RESET = "\033[0m"    
HIJAU = "\033[92m"     
MERAH = "\033[91m"    
BIRU = "\033[94m"     

def tambah_tugas(tasks):
        tugas_baru = input("Masukkan nama tugas (pisahkan dengan koma jika lebih dari satu): ")
        tugas_list = [tugas.strip() for tugas in tugas_baru.split(",")]
        tasks.extend(tugas_list)
        print(f"{HIJAU}{len(tugas_list)} tugas berhasil ditambahkan.{RESET}")
        
def lihat_tugas(tasks):
    if tasks:
        print(f"\n{BIRU}Daftar tugas: {RESET}")
        for idx, tasks in enumerate(tasks, 1):
            print(f"{BIRU}{idx}. {tasks}{RESET}")
    else:
        print(f"{MERAH}\nTidak ada tugas{RESET}")
            
def edit_tugas(tasks):
    lihat_tugas(tasks)
    if tasks:
        try:
            input_nomer = input(f"{BIRU}\nMasukkan nomor tugas yang ingin diedit (pisahkan dengan koma): {RESET}")
            nomor_list = [int(nomer.strip()) - 1 for nomer in input_nomer.split(',')]
            
            for no_tugas in nomor_list:
                if 0 <= no_tugas < len(tasks):
                    tugas_baru = input(f"Masukkan tugas baru untuk tugas nomor {no_tugas + 1}: ")
                    tasks[no_tugas] = tugas_baru
                    print(f"{HIJAU}Tugas nomor {no_tugas + 1} berhasil diperbarui.{RESET}")
                else:
                    print(f"{MERAH}Nomor tugas {no_tugas + 1} tidak terdeteksi.{RESET}")            
        except ValueError:
            print(f"{MERAH} Input tidak valid.{RESET}")
            
def hapus_tugas(tasks):
    lihat_tugas(tasks)
    if tasks:
        try:
            input_nomer = input("\nMasukkan nomor tugas yang ingin dihapus (pisahkan dengan koma), atau ketik 'all' untuk menghapus semua: ")
            
            if input_nomer.strip().lower() == "all":
                konfirmasi = input("Apakah Anda yakin ingin menghapus semua tugas? (y/n): ").strip().lower()
                if konfirmasi == "y":
                    tasks.clear()
                    print(f"{HIJAU}Semua tugas berhasil dihapus.{RESET}")
                else:
                    print(f"{MERAH}Penghapusan semua tugas dibatalkan.{RESET}")
            else:
                nomer_list = sorted([int(nomer.strip()) - 1 for nomer in input_nomer.split(',')], reverse=True)

                for no_tugas in nomer_list:
                    if 0 <= no_tugas < len(tasks):
                        tasks.pop(no_tugas)
                        print(f"{HIJAU}Tugas nomor {no_tugas + 1} berhasil dihapus.{RESET}")
                    else:
                        print(f"{MERAH}Nomor tugas {no_tugas + 1} tidak valid.{RESET}")
                    
        except ValueError:
            print(f"{MERAH}Input tidak valid.{RESET}")

         
def menu():
    tasks = []
    while True:
         print("\n=============== Daftar Tugas ===============")
         print("1. Tambah tugas\n2. Lihat tugas\n3. Edit tugas\n4. Hapus tugas\n5. Keluar")
    
         pilihan = input("Pilih opsi (1-5): ")
    
         if pilihan == "1":
           tambah_tugas(tasks)
         elif pilihan == "2":
           lihat_tugas(tasks)
         elif pilihan == "3":
           edit_tugas(tasks)
         elif pilihan == "4":
            hapus_tugas(tasks)
         elif pilihan == "5":
            print(f"{HIJAU}Keluar program.{RESET}")
            break
         else:
            print(f"{MERAH}Inputan tidak valid. Mohon masukkan angka.{RESET}")
            
if __name__ == "__main__":
    menu()