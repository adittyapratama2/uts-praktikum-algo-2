# Soal 2: Mengonversi Detik ke Jam, Menit, dan Detik
waktu = int(input("Masukkan waktu dalam detik: "))
jam = waktu // 3600
menit = (waktu % 3600) // 60
detik = waktu % 60
print(f"Hasil konversi: {jam} jam, {menit} menit, {detik} detik")

#Jerry Hilman Firmansyah 2203010512
#perogram ini dibuat untuk mengkonversi detik -> jam, menit, dan detik
#menggunakan 1 inputan dan ada 3 buah tipe data berbentuk initeger
