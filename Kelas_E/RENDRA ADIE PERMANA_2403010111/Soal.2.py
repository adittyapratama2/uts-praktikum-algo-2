# Meminta input waktu dalam detik dari user
waktu_detik = int(input("Masukkan waktu dalam detik: "))

# Menghitung jumlah jam, menit, dan detik
jam = waktu_detik // 3600
menit = (waktu_detik % 3600) // 60
detik = waktu_detik % 60

# Menampilkan hasil konversi
print(f"Hasil untuk konversi: {jam} jam, {menit} menit, {detik} detik")

#Nama_Rendra_Adie_Permana
#NIM_2403010111