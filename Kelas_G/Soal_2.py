# Program untuk mengonversi detik ke jam, menit, dan detik

# Meminta input dari pengguna
detik = int(input("Masukkan waktu dalam detik: "))

# Menghitung jam, menit, dan detik
jam = detik // 3600
detik_sisa = detik % 3600
menit = detik_sisa // 60
detik_terakhir = detik_sisa % 60

# Menampilkan hasil konversi
print(f"Hasil konversi: {jam} jam, {menit} menit, {detik_terakhir} detik")
