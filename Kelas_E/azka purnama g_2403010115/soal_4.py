
print("-----Menghitung huruf konsonan-----")
print(" ")

# meminta input kalimat dari user
kalimat = input('masukan kalimat: ')

# mengubah kalimat yang diinput menjadi hurup kecil
string = kalimat.lower()

# menjumlahkan hurup dalam kalimat yang diinput 
count = 0

# daftar hurup yang akan diabaikan dalam perhitungan
list1 = ["a","i","u","e","o"]

# mengecek setiap karakter dalam kalimat yang diinput
for char in string:

    #mengecek apakah karakter adalah hurup dan bukan vokal
    if char in list1:
        count = count+1

# menampilkan hasil dari perhitungan konsonan diatas
print("jumlah huruf vokal adalah:",count)