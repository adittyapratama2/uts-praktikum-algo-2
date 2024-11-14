# Meminta input kalimat dari pengguna
kalimat = input("Masukkan kalimat: ")

# Daftar huruf vokal
vokal = "aeiouAEIOU"

# Inisialisasi variabel untuk menghitung konsonan
jumlah_konsonan = 0

# Iterasi setiap karakter dalam kalimat
for char in kalimat:
    # Mengecek apakah karakter adalah huruf dan bukan vokal
    if char.isalpha() and char not in vokal:
        jumlah_konsonan += 1

# Menampilkan jumlah huruf konsonan
print("Jumlah huruf konsonan dalam kalimat:", jumlah_konsonan)
