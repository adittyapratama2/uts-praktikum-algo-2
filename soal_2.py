# meminta input waktu dalam detik
detik = int(input("masukan waktu dalam detik: "))

# menghitung jumlah jam, menit, dan detik
jam = detik // 3600 # 1 jam = 3600 detik
detik_sisa = detik % 3600
menit = detik_sisa // 60 # 1 menit = 60 detik
detik_akhir = detik_sisa % 60

# menampilkan hasil konversi
print(f"waktu{jam} jam, {menit} menit, {detik_akhir} detik")
