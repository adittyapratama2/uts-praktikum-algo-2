 # Meminta pengguna untuk memasukkan sebuah kalimat
kalimat = input("Masukkan sebuah kalimat: ")

# Mendefinisikan huruf vokal
vokal = "aeiouAEIOU"

# Menghitung jumlah huruf konsonan
jumlah_konsonan = 0

for huruf in kalimat:
    if huruf.isalpha() and huruf not in vokal:
        jumlah_konsonan += 1

# Menampilkan jumlah huruf konsonan
print("Jumlah huruf konsonan dalam kalimat tersebut adalah:", jumlah_konsonan)