print("Selamat datang di program konversi suhu!")
print("Pilih opsi konversi:")
print("1. Celsius ke Fahrenheit")
print("2. Fahrenheit ke Celsius")

while True:
    try:
        pilihan = int(input("Masukkan pilihan Anda (1/2): "))
        if pilihan in [1, 2]:
            break
        else:
            print("Harap masukkan 1 atau 2.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka 1 atau 2.")

while True:
    try:
        suhu = float(input("Masukkan suhu: "))
        break
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

if pilihan == 1:
    if suhu < -273.15:
        print("Suhu tidak valid! Suhu tidak boleh lebih rendah dari -273.15°C (nol absolut).")
    else:
        hasil = (suhu * 9/5) + 32
        print(f"{suhu}°C sama dengan {hasil:.2f}°F")
else:
    if suhu < -459.67:
        print("Suhu tidak valid! Suhu tidak boleh lebih rendah dari -459.67°F (nol absolut).")
    else:
        hasil = (suhu - 32) * 5/9
        print(f"{suhu}°F sama dengan {hasil:.2f}°C")
