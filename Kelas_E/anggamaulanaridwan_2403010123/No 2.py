#Meminta input waktu dalam detik dari pengguna
waktu_detik = int(input("Masukkan waktu dalam detik anda: "))

#Menghitung jumlah jam, menit, dan detik
jam = waktu_detik // 3600
menit = (waktu_detik % 3600) // 60
detik = waktu_detik % 60

#Menampilkan hasil konversinya
print(f"Hasil untuk konversi adalah: {jam} jam, {menit} menit, {detik} detik")