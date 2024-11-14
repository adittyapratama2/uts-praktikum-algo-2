# ZIyan Fathu Rohman
# 2403010175

# mengonversi detik ke jam, menit, dan detik

waktu_dalam_detik = float(input("masukkan waktu dalam detik : "))

# menghitung jam, menit, dan detik

jam = waktu_dalam_detik//3600
sisa_detik = waktu_dalam_detik%3600
menit = sisa_detik//60
detik = waktu_dalam_detik

# tampilkan hasil konversi 
print (f"waktu yang dimasukakan adala {jam} jam, {menit} menit, dan {detik} detik")