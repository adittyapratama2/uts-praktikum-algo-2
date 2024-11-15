#imanuel tanu senjaya 2403010143
# Program untuk mengonversi detik ke jam, menit, dan detik

# Meminta input waktu dalam detik
waktu_detik = int(input("Masukkan waktu dalam detik: "))

# Menghitung jam, menit, dan detik
jam = waktu_detik // 3600               # 1 jam = 3600 detik
sisa_detik = waktu_detik % 3600         # Sisa detik setelah dikurangi jam
menit = sisa_detik // 60                # 1 menit = 60 detik
detik = sisa_detik % 60                 # Sisa detik setelah dikurangi menit

# Menampilkan hasil konversi
print(f"Hasil konversi: {jam} jam, {menit} menit, {detik} detik")
