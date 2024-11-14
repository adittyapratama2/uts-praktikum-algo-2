# Meminta pengguna untuk memasukkan sebuah kalimat
kalimat = input("Masukkan sebuah kalimat: ")

# Daftar huruf vokal
vokal = "aeiouAEIOU"

# Menghitung jumlah huruf konsonan
jumlah_konsonan = 0
for huruf in kalimat:
    if huruf.isalpha() and huruf not in vokal:
        jumlah_konsonan += 1

# Menampilkan hasil
print("Jumlah huruf konsonan dalam kalimat:", jumlah_konsonan)