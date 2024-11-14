'''
Agung Ilham Setiyadi
2403010090
Mengonversi Detik ke Jam, Menit, dan Detik
'''

waktu_dalam_detik = int(input("Masukan detik: "))
jam = waktu_dalam_detik // 3600
menit = (waktu_dalam_detik % 3600) // 60
detik = waktu_dalam_detik % 60

print("Masukan waktu dalam detik: ",waktu_dalam_detik)
print("Hasil konversi: ",jam,"jam",menit,"menit",detik,"detik")