#menghitung jam melalui detik
total_detik = int (input("masukan waktu dalam bentuk detik: "))
#total detik
jam = total_detik//3600
sisa_detik = total_detik % 3600
#sisa_detik
menit= sisa_detik //60
detik= sisa_detik % 60
#hasil konversi jam, menit, detik
print(f"Hasil konversi:{jam}jam, {menit}menit, {detik}detik")

