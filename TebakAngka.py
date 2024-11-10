import random
angka_rahasia = random.randint(1, 10)
cobaTebak = 0

print("Selamat Datang dipermainan Tebak Angka")
print("Cluenya saya memiliki angka dari 1-10, coba tebak angkanya!")

while True:
    try:
        tebakan = int (input("Masukkan angka yang kamu pilih: "))
        cobaTebak += 1
        
        if tebakan < angka_rahasia:
            print("Tebakanmu terlalu rendah. Coba tebak kembali!")
        elif tebakan > angka_rahasia:
            print("Tebakanmu terlalu tinggi. Coba tebak kembali!")
        else :
            print("Selamat tebakan kamu benar")
            break
    except ValueError:
        print("Input tidak valid. Coba masukkan angka yang benar!")