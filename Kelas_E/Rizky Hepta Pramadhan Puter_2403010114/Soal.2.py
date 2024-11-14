# Untuk meminta input waktu dalam detik dari user
waktu_detik = int(input("Masukkan waktu dalam detik: "))

# Untuk menghitung jumlah jam, menit, dan detik
jam = waktu_detik // 3600
menit = (waktu_detik % 3600) // 60
detik = waktu_detik % 60

# Untuk menampilkan hasil konversi
print(f"Hasil untuk konversi: {jam} jam, {menit} menit, {detik} detik")

#Nama_Rizky Hepta Pramadhan Putera
#NIM_2403010114