# Program untuk menghitung jumlah huruf konsonan dalam sebuah kalimat

kalimat = input("Masukkan sebuah kalimat: ")

jumlah_konsonan = 0

# Daftar huruf vokal
vokal = "aeiouAEIOU"

# Menghitung jumlah konsonan
for huruf in kalimat:
    if huruf.isalpha() and huruf not in vokal:  
        jumlah_konsonan += 1

print(f"Jumlah huruf konsonan dalam kalimat tersebut adalah: {jumlah_konsonan}")