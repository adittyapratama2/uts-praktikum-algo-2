# Nama: Asep Zarkasih Noor
# NIM: 2303010172
# Deskripsi: Program Menghitung Jumlah Huruf Konsonan dalam Kalimat

# Meminta pengguna memasukkan kalimat
kalimat = input("Masukkan kalimat: ")

# Daftar huruf vokal
vokal = "aeiouAEIOU"

# Menghitung jumlah huruf konsonan
jumlah_konsonan = 0
for huruf in kalimat:
    if huruf.isalpha() and huruf not in vokal:
        jumlah_konsonan += 1

# Menampilkan hasil
print("Jumlah huruf konsonan:", jumlah_konsonan)
