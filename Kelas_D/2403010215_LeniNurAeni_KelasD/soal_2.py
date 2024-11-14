#soal 2
#Mengonversi Detik ke Jam, Menit, dan Detik
total_detik = int(input("Masukkan waktu dalam bentuk detik: "))
jam = total_detik // 3600
sisa_detik = total_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60 
print(f"Hasil konversi: {jam} jam, {menit} menit, {detik} detik")