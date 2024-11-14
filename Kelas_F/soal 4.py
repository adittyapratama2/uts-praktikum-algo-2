# Meminta pengguna untuk memasukkan kalimat
kalimat = input("Masukkan kalimat: ")

# Mengonversi kalimat menjadi huruf kecil agar mudah diidentifikasi
kalimat = kalimat.lower()

# Menentukan huruf vokal dan inisialisasi jumlah konsonan
vowels = "aeiou"
jumlah_konsonan = 0

# Menghitung jumlah huruf konsonan
for huruf in kalimat:
    if huruf.isalpha() and huruf not in vowels:
        jumlah_konsonan += 1

# Menampilkan hasil
print("Jumlah huruf konsonan:", jumlah_konsonan)

#Program meminta input berupa kalimat dan mengonversinya ke huruf kecil.

#Mendefinisikan huruf vokal dalam variabel vowels.

#Menginisialisasi variabel jumlah_konsonan untuk menghitung konsonan.

#Menggunakan loop untuk mengecek setiap karakter, menghitung huruf yang termasuk konsonan.

#Menampilkan jumlah huruf konsonan.

#FahmiZamzamZawahir_2403010132
