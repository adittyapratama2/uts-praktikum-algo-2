#NAMA : MUHAMMAD DARIS RIF'AN RAMADHAN
#NIM  : 2403010164
#  Meminta input waktu dalam detik
total_detik = int(input("Masukkan waktu dalam detik: "))

# Menghitung jam, menit, dan detik
jam = total_detik // 3600
sisa_detik = total_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

# Menampilkan hasil
print(f"{total_detik} detik sama dengan {jam} jam, {menit} menit, dan {detik} detik.")