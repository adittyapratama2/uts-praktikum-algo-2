detik = int(input('Masukkan jumlah detik: '))

konversi_jam = detik // 3600
sisa_detik = detik % 3600
konversi_menit = sisa_detik // 60
hasil_detik = sisa_detik % 60

print(f'Hasil konversinya adalah {konversi_jam} jam, {konversi_menit} menit, {hasil_detik} detik.')