#imanuel tanu senjaya 2403010143
# Program untuk menghitung jumlah huruf konsonan dalam kalimat

# Program untuk menghitung jumlah huruf konsonan dalam kalimat

# Meminta input kalimat dari pengguna
kalimat = input("Masukkan kalimat: ")

# Menentukan huruf vokal yang harus diabaikan
vokal = "aeiouAEIOU"

# Inisialisasi penghitung konsonan
jumlah_konsonan = 0

# Iterasi setiap karakter dalam kalimat
for char in kalimat:
    # Cek jika karakter adalah huruf dan bukan vokal
    if char.isalpha() and char not in vokal:
        jumlah_konsonan += 1

# Menampilkan hasil
print(f"Jumlah huruf konsonan: {jumlah_konsonan}")
