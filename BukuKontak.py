kontak = {}

def tambah_kontak(nama, nomor):
    if nama in kontak:
        print(f"Kontak dengan nama {nama} sudah ada.")
    else:
        kontak[nama] = nomor
        print(f"Kontak {nama} berhasil ditambahkan.")

def cari_kontak(nama):
    if nama in kontak:
        print(f"Nomor kontak {nama}: {kontak[nama]}")
    else:
        print(f"Kontak {nama} tidak ditemukan.")

def tampilkan_semua_kontak():
    if not kontak:
        print("Tidak ada kontak yang tersimpan.")
    else:
        print("Daftar Kontak:")
        for nama, nomor in kontak.items():
            print(f"{nama}: {nomor}")

def hapus_kontak(nama):
    if nama in kontak:
        del kontak[nama]
        print(f"Kontak {nama} berhasil dihapus.")
    else:
        print(f"Kontak {nama} tidak ditemukan.")

def menu():
    while True:
        print("\n--- Aplikasi Kontak ---")
        print("1. Tambah Kontak")
        print("2. Cari Kontak")
        print("3. Tampilkan Semua Kontak")
        print("4. Hapus Kontak")
        print("5. Keluar")
        
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            nama = input("Masukkan nama kontak: ")
            nomor = input("Masukkan nomor kontak: ")
            tambah_kontak(nama, nomor)
        elif pilihan == "2":
            nama = input("Masukkan nama kontak yang ingin dicari: ")
            cari_kontak(nama)
        elif pilihan == "3":
            tampilkan_semua_kontak()
        elif pilihan == "4":
            nama = input("Masukkan nama kontak yang ingin dihapus: ")
            hapus_kontak(nama)
        elif pilihan == "5":
            print("Terima kasih telah menggunakan aplikasi kontak.")
            break
        else:
            print("Opsi tidak valid! Harap pilih antara 1-5.")

menu()
