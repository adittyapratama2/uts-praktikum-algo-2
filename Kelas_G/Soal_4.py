# Meminta input dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Mendefinisikan huruf vokal
vokal = "aeiouAEIOU"

# Menghitung jumlah konsonan
jumlah_konsonan = 0
for huruf in kalimat:
    if huruf.isalpha() and huruf not in vokal:  # Hanya menghitung huruf alfabet non-vokal
        jumlah_konsonan += 1

# Menampilkan hasil
print("Jumlah huruf konsonan dalam kalimat:", jumlah_konsonan)
