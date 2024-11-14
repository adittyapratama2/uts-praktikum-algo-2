#meminta penguna memasukan sebuah kalimat
kalimat = input("masukan sebuah kalimat:")

# mengonversikan kalimat ke huruf kecil untuk memudahkan perhitungan
kalimat=kalimat.lower()

# mendefinisikan huruf vokal
vokal="aiueo"

# inisisalisasi untuk menghitung jumblah konsonan
jumblah_konsonan = 0

# loop untuk menghitung jumblah huruf konsonan
for huruf in kalimat:
    if huruf.isalpha() and huruf not in vokal:
        jumblah_konsonan += 1
        # menampilkan jumblah konsonan
        print("jumblah konsonan dalam dalam kalimat tersebut adalah:", jumblah_konsonan)
        