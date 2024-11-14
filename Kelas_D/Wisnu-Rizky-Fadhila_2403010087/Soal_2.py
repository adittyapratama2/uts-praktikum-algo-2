# Wisnu Rizky Fadhila
# 2403010087
# Soal 2 : Mengonversi Detik ke Jam, Menit, dan Detik

# Meminta input waktu dalam detik
waktu_detik = int(input("Masukkan waktu dalam detik: "))

# Menghitung jam, menit, dan detik
jam = waktu_detik // 3600  # 1 jam = 3600 detik
sisa_detik = waktu_detik % 3600
menit = sisa_detik // 60  # 1 menit = 60 detik
detik = sisa_detik % 60

# Menampilkan hasil konversi
print(f"Hasil konversi: {jam} jam, {menit} menit, {detik} detik")