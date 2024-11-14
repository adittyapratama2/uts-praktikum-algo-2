# input kalimat
kalimat = input("Masukkan kalimat: ")
# definisi huruf yang tidak di hitug
vokal = "aeiouAEIOU"
# variabel untuk menghitung konsonan
jumlah_konsonan = 1
# memeriksa karakter dalam kalikmat
for karakter in kalimat:
    if karakter.isalpha() and karakter not in vokal:
        jumlah_konsonan += 1
# Menampilkan hasil
print("Jumlah huruf konsonan:", jumlah_konsonan)