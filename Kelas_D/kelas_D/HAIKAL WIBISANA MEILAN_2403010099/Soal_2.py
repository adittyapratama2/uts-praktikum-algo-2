# Meminta pengguna untuk memasukkan waktu dalam detik
waktu_detik = int(input("Masukkan waktu dalam detik: "))

# Menghitung jam, menit, dan detik
jam = waktu_detik // 3600
sisa_detik = waktu_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

# Menampilkan hasil dalam format jam, menit, dan detik
print(f"Format waktu: {jam} jam, {menit} menit, {detik} detik")