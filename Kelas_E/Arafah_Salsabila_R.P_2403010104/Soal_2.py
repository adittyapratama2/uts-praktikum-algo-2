#Meminta input detik
detik = int(input("Masukan waktu dalam detik: "))
#menghitung jam, menit,dan detik
jam = detik // 3600 #1 jam = 3600 detik
sisa_detik = detik % 3600
menit = sisa_detik // 60 #1 menit = 60 detik
detik = sisa_detik % 60
print("Hasil konversi: ", jam, "jam, ", menit,"menit,", detik, "detik")
