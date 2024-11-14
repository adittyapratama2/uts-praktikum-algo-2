# Masukan waktu dalam detik
detik = int(input("Masukan Waktu Dalam Detik: "))
# mengkonversikan ke jam 
jam = detik // 3600 # menghitung jumlah jam dari detik yang dimasukan
sisa_detik = detik % 3600 # menghitung sisa detik setelah di konversikan ke jam
#mengkonversikan ke menit
menit = sisa_detik // 60 # menghitung jumlah menit dari sisa detik
detik = sisa_detik % 60 # menghitung jumlah detik dari sisa detik
# Menampilkan hasil konversi 
print(f"Hasil Konversi: {jam} Jam, {menit} Menit, {detik} Detik")