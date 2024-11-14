# Program untuk mengonversi detik ke jam, menit, dan detik
waktu_detik = int(input("Masukkan waktu dalam detik: "))
jam = waktu_detik // 3600
sisa_detik = waktu_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60
print(f"Hasil konversi: {jam} jam, {menit} menit, {detik} detik")
