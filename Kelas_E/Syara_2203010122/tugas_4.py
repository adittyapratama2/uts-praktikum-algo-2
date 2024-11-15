#Syara
#2203010122

kalimat = input("Masukan sebuah kalimat:")

# mengonversikan kalimat ke huruf kecil untuk memudahkan perhitungan
kalimat = kalimat.lower()

# mendefinisikan huruf vokal
vokal = "aiueo"

# inisialisasi untuk menghitung jumlah konsonan
jumlah_konsonan = 0

# loop untuk menghitung jumlah huruf konsonan
for huruf in kalimat:
    if huruf.isalpha() and huruf not in vokal:
        jumlah_konsonan += 1

# menampilkan jumlah konsonan
print("Jumlah konsonan dalam kalimat tersebut adalah:", jumlah_konsonan)
