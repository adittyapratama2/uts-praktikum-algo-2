print("\n--- Mengonversi Detik ke Jam, Menit, dan Detik ---\n")

detik = int(input("Masukkan waktu dalam detik: "))

jam = detik // 3600
detik_sisa = detik % 3600
menit = detik_sisa // 60
detik_terakhir = detik_sisa % 60

print(f"Hasil konversi : {jam} jam, {menit} menit, {detik_terakhir} detik")