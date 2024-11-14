detik = int(input("masukan detik waktu : "))
jam = detik // 3600
sisa_detik = detik % 3600 
menit = sisa_detik // 60 
format_waktu = sisa_detik % 60
print(f"hasil nya : {jam} jam, {menit} menit, {format_waktu} detik")