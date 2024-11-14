# Meminta input dari pengguna
total_detik = int(input("Masukkan waktu dalam detik: "))

# Menghitung jam, menit, dan detik
jam = total_detik // 3600  # 1 jam = 3600 detik
sisa_detik = total_detik % 3600
menit = sisa_detik // 60   # 1 menit = 60 detik
detik = sisa_detik % 60

# Menampilkan hasil
print(f"Waktu: {jam} jam, {menit} menit, {detik} detik")
