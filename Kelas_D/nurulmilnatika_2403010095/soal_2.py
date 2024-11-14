#nama:nurul milnatika
#NIM: 2403010095

total_detik = int(input("Masukkan waktu dalam bentuk detik: "))
jam = total_detik // 3600
sisa_detik = total_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60 
print(f"Hasil konversi: {jam} jam, {menit} menit, {detik} detik")
