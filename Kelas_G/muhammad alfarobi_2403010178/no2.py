waktu_detik = int(input("Masukkan waktu dalam detik: "))
jam = waktu_detik // 3600  
waktu_detik %= 3600        
menit = waktu_detik // 60 
detik = waktu_detik % 60
print(f"Hasil konversi: {jam} jam, {menit} menit, {detik} detik")
