# Meminta pengguna untuk memasukkan waktu dalam detik
waktu_detik = int(input("Masukkan waktu dalam detik: "))

# Menghitung jumlah jam, menit, dan detik
jam = waktu_detik // 3600           # 1 jam = 3600 detik
sisa_detik = waktu_detik % 3600      # Sisa detik setelah dihitung jam
menit = sisa_detik // 60             # 1 menit = 60 detik
detik = sisa_detik % 60              # Sisa detik setelah dihitung menit

# Menampilkan hasil konversi
print(f"Hasil konversi: {jam} jam, {menit} menit, {detik} detik")
