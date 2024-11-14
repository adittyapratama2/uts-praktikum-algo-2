#Nama: Muhammad Andi Abdillah
#NIM: 2403010120

#Mengonversi Detik ke Jam, Menit, dan Detik
detik = int(input("Masukkan waktu dalam detik: "))

#Rumus Konversi detik ke Jam, menit, Detik
jam = detik // 3600
menit = (detik % 3600) // 60
detik = detik % 60

#hasil konversi
print(f"Hasil konversi: {jam} jam, {menit} menit, {detik} detik")