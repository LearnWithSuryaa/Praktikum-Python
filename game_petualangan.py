print("Selamat datang di petualangan seru ini!")
print("Kamu adalah seorang petualang yang sedang menjelajahi dunia penuh misteri.")
print("Apa yang akan kamu lakukan?")

pilihan1 = input("Kamu tiba di sebuah persimpangan jalan. Pilih kiri atau kanan (ketik 'kiri' atau 'kanan'): ").lower()

if pilihan1 == "kiri":
    print("\nKamu berjalan ke kiri dan menemukan sebuah gua yang gelap. Suasana agak mencekam di sana.")
    pilihan2 = input("Mau masuk ke gua itu (ketik 'masuk') atau terus jalan (ketik 'lanjut')? ").lower()

    if pilihan2 == "masuk":
        print("\nKamu masuk ke dalam gua dan menemukan harta karun yang tersembunyi! Wah, kamu menang besar!")
    elif pilihan2 == "lanjut":
        print("\nKamu lanjutkan perjalanan dan menemukan sebuah desa yang damai. Warga di sana menyambutmu dengan hangat!")
    else:
        print("Hmm, pilihanmu nggak jelas. Coba pilih antara 'masuk' atau 'lanjut'.")

elif pilihan1 == "kanan":
    print("\nKamu ke kanan dan tiba di tepi danau yang indah. Airnya jernih banget!")
    pilihan3 = input("Mau berenang nyebrang danau (ketik 'berenang') atau jalan santai di sepanjang tepi (ketik 'jalan')? ").lower()

    if pilihan3 == "berenang":
        print("\nKamu berenang dan berhasil nyebrang, tapi agak capek. Untung ada kapal lewat yang nyelamatin kamu!")
    elif pilihan3 == "jalan":
        print("\nKamu jalan santai sepanjang danau dan menemukan sebuah kota kecil yang penuh petualangan. Siap-siap, petualangan baru dimulai!")
    else:
        print("Eh, pilihannya nggak ada di situ! Coba pilih 'berenang' atau 'jalan'.")

else:
    print("Pilihanmu nggak valid, deh. Pilih antara 'kiri' atau 'kanan' dong.")
