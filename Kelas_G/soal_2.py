# Meminta pengguna untuk memasukkan waktu dalam detik
detik_total = int(input("Masukkan waktu dalam detik: "))

# Menghitung jumlah jam, menit, dan detik
jam = detik_total // 3600
sisa_detik = detik_total % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

# Menampilkan hasil konversi
print(f"Waktu {detik_total} detik adalah {jam} jam, {menit} menit, dan {detik} detik.")