# Program untuk menghitung jumlah huruf konsonan dalam kalimat

# Meminta input kalimat dari pengguna
kalimat = input("Masukkan kalimat: ")

# Menentukan huruf vokal yang harus dihindari
vokal = "aeiouAEIOU"

# Menghitung jumlah huruf konsonan
jumlah_konsonan = 0

# Iterasi setiap karakter dalam kalimat
for char in kalimat:
    if char.isalpha() and char not in vokal:  # Mengecek apakah karakter adalah huruf dan bukan vokal
        jumlah_konsonan += 1

# Menampilkan hasil jumlah konsonan
print("Jumlah huruf konsonan:", jumlah_konsonan)
