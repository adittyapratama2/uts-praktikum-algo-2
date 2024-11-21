# Meminta pengguna untuk memasukkan sebuah kalimat
kalimat = input("Masukkan kalimat: ")

# Daftar huruf vokal
vokal = "aeiouAEIOU"

# Variabel untuk menghitung jumlah konsonan
jumlah_konsonan = 0

# Mengecek setiap karakter dalam kalimat
for char in kalimat:
    if char.isalpha() and char not in vokal:  # Cek apakah karakter adalah huruf dan bukan vokal
        jumlah_konsonan += 1

# Menampilkan jumlah huruf konsonan
print("Jumlah huruf konsonan:", jumlah_konsonan)
