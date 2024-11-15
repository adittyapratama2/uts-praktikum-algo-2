total_detik= int(input("masukan waktu dalam detik:"))
jam=total_detik //3600
sisa_detik=total_detik % 3600
menit=sisa_detik // 60
detik=sisa_detik % 60
print(f"hasil konversi: {jam}jam, {menit}menit, {detik}detik")