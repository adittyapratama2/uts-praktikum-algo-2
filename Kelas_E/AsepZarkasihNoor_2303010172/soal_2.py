# Nama: Asep Zarkasih Noor
# NIM: 2303010172
# Deskripsi: Program Mengonversi Detik ke Jam, Menit, dan Detik

# Meminta pengguna memasukkan waktu dalam detik
total_detik = int(input("Masukkan waktu dalam detik: "))

# Menghitung jumlah jam, menit, dan detik
jam = total_detik // 3600  # 1 jam = 3600 detik
sisa_detik = total_detik % 3600
menit = sisa_detik // 60  # 1 menit = 60 detik
detik = sisa_detik % 60

# Menampilkan hasil konversi
print(f"Hasil konversi: {jam} jam, {menit} menit, {detik} detik")
