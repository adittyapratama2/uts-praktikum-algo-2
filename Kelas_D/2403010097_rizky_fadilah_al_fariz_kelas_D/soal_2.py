#soal no 2
# Fungsi untuk mengonversi detik ke jam, menit, dan detik
def konversi_waktu(total_detik):
    jam = total_detik // 3600
    sisa_detik = total_detik % 3600
    menit = sisa_detik // 60
    detik = sisa_detik % 60
    return jam, menit, detik

# Meminta pengguna untuk memasukkan waktu dalam detik
total_detik = int(input("Masukkan waktu dalam detik: "))

# Mengonversi detik ke jam, menit, dan detik
jam, menit, detik = konversi_waktu(total_detik)

# Menampilkan hasil konversi
print(f"{total_detik} detik setara dengan {jam} jam, {menit} menit, dan {detik} detik.")