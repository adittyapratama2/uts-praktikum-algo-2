#Program mengonversi waktu dari detik ke jam, menit, dan detik

#input dari pengguna
waktu_dalam_detik = int(input("Masukan waktu dalam detik: "))

#Menghitung jam, menit, dan detik
jam = waktu_dalam_detik // 3600
sisa_detik = waktu_dalam_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

#menamilkan hasil konversi
print(f"Hasil konversi: {jam} jam, {menit} menit, {detik} detik")
