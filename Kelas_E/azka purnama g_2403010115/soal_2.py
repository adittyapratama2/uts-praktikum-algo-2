#subtitel
print("-----Konversi detik,menit,jam-----")
print(" ")

# buat meminta user meninput waktu dalam per detiknyo
waktu_detik = int(input("Masukkan waktu dalam detik: "))

# buat menghitung jumlah semua jam, menit, dan detik
jam = waktu_detik // 3600
menit = (waktu_detik % 3600) // 60
detik = waktu_detik % 60

# menampilhan hasil dari kodingan diatas
print(f"Hasil untuk konversi: {jam} jam, {menit} menit, {detik} detik")
