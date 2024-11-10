num1 = int(input("Masukkan angka pertama: "))
num2 = int(input("Masukkan angka kedua: "))

penjumlahan = num1 + num2
pengurangan = num1 - num2
perkalian = num1 * num2
def pembagian(num1, num2):
    try:
        hasil = num1 / num2
        return hasil
    except ZeroDivisionError:
        return "Error angka tidak bisa dibagi dengan 0!"

print("Hasil penjumlahan:", penjumlahan)
print("Hasil pengurangan:", pengurangan)
print("Hasil perkalian:", perkalian)
print("Hasil pembagian:", pembagian(num1, num2))