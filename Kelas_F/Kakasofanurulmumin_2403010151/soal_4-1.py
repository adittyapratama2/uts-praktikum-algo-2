# Program untuk menghitung jumlah huruf konsonan dalam sebuah kalimat

# Meminta input dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Daftar huruf vokal
vokal = "aeiouAEIOU"

# Menghitung jumlah konsonan
jumlah_konsonan = 0
for huruf in kalimat:
    if huruf.isalpha() and huruf not in vokal:  # Memeriksa apakah huruf adalah alfabet dan bukan vokal
        jumlah_konsonan += 1

# Menampilkan hasil
print(f"Jumlah huruf konsonan dalam kalimat: {jumlah_konsonan}")

#nama_kaka_sofa_nurul_mu'min
#nim_2403010151
