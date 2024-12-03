RESET = "\033[0m"    
HIJAU = "\033[92m"     
MERAH = "\033[91m"  

daftar_pertanyaan = [
    {
        "soal": "Dimana ibu kota Indonesia?",
        "pilihan": ["A. IKN", "B. Jakarta", "C. Surabaya", "D. Yogyakarta"],
        "jawaban": "A"
    },
    {
        "soal": "Siapa Presiden pertama Indonesia?",
        "pilihan": ["A. Prabowo", "B. Soekarno", "C. Suharto", "D. Jokowi"],
        "jawaban": "B"
    },
    {
        "soal": "Apa warna bendera Indonesia?",
        "pilihan": ["A. Merah Putih", "B. Merah Biru", "C. Putih Merah", "D. Biru Putih"],
        "jawaban": "A"
    }
]

skor = 0

for pertanyaan_item in daftar_pertanyaan:
    print(pertanyaan_item["soal"]) 
    for pilihan in pertanyaan_item["pilihan"]:
        print(pilihan)  

    jawaban_user = input("Pilih jawaban (A/B/C/D): ").upper()

    if jawaban_user == pertanyaan_item["jawaban"]:
        print(f"{HIJAU}Jawaban Anda benar!\n{RESET}")
        skor += 1  
    else:
        print(f"{MERAH}Jawaban Anda salah.\n{RESET}")

print(f"Skor Anda: {skor}/{len(daftar_pertanyaan)}")
