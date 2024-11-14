# Nama: Muhamad Rif'atul Akbar
# NIM: 2403010091
# Kelas: D(TI) 2024
# Program tentang cara Mengonversi Detik ke Jam, Menit, dan Detik

print("Mengonversi Detik ke Jam, Menit, dan Detik")

Detik = int(input("Masukkan waktu dalam Detik: "))
jam = Detik//3600
menit = (Detik%3600)//60
detik = Detik%60

print("Hasil konversi: ",jam,"jam",menit,"menit",detik,"detik")