# Meminta input kalimat dari pengguna
kalimat = input("Masukkan kalimat: ")

# Inisialisasi variabel untuk menghitung jumlah konsonan
jumlah_konsonan = 0

# Daftar huruf vokal
vokal = "aeiouAEIOU"

# Iterasi setiap karakter dalam kalimat
for karakter in kalimat:
    # Memeriksa apakah karakter adalah huruf dan bukan vokal
    if karakter.isalpha() and karakter not in vokal:
        jumlah_konsonan += 1

# Menampilkan jumlah huruf konsonan
print("Jumlah huruf konsonan:", jumlah_konsonan)
