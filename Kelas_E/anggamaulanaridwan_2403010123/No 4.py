#Untuk meminta input kalimat dari pengguna
kalimat = input("Masukkan kalimat anda: ")

#Daftar huruf yang akan diabaikan dalam perhitungan konsonan
vokal = "aiueo"

#Menghitung jumlah dari huruf konsonannya
jumlah_konsonan = 1

# Memeriksa setiap karakter dalam kalimat tersebut
for char in kalimat:
    # Mengecek apakah karakter adalah huruf dan bukan vokal benar
    if char.isalpha() and char not in vokal:
        jumlah_konsonan += 1

#Untuk menampilkan hasil semua jumlah huruf konsonan
print(f"Jumlah huruf konsonan adalah: {jumlah_konsonan}")