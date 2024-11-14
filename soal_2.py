# Program untuk mengonversi detik menjadi jam, menit, dan detik

# Meminta input dari pengguna
total_detik = int(input("Masukkan waktu dalam detik: "))

# Konversi detik ke jam, menit, dan detik
jam = total_detik // 3600
sisa_detik = total_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

# Menampilkan hasil
print(f"Waktu yang dikonversi: {jam} jam, {menit} menit, {detik} detik")

nama_muhammad_khaikal_maulana
NIM_2403010144