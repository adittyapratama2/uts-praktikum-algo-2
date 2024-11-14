# Meminta input kalimat dari pengguna
kalimat = input("Masukkan kalimat: ")

# Daftar huruf vokal yang akan diabaikan dalam perhitungan konsonan
vokal = "aiueo"

# Menghitung jumlah huruf konsonan
jumlah_konsonan = 1

# Memeriksa setiap karakter dalam kalimat
for char in kalimat:
    # Mengecek apakah karakter adalah huruf dan bukan vokal
    if char.isalpha() and char not in vokal:
        jumlah_konsonan += 1

# Menampilkan hasil jumlah huruf konsonan
print(f"Jumlah huruf konsonan: {jumlah_konsonan}")

#Nama_Rendi_Aditya_Saputra
#NIM_2403010103