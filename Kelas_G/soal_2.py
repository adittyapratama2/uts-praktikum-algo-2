# Meminta input waktu dalam detik dari pengguna
detik = int(input("Masukkan waktu dalam detik: "))

# Menghitung jam, menit, dan detik
jam = detik // 3600          # 1 jam = 3600 detik
detik_sisa = detik % 3600
menit = detik_sisa // 60     # 1 menit = 60 detik
detik_akhir = detik_sisa % 60

# Menampilkan hasil konversi
print(f"Hasil konversi: {jam} jam, {menit} menit, {detik_akhir} detik")
