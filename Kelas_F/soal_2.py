def konversi_waktu(total_detik):
    jam = total_detik // 3600
    sisa_detik = total_detik % 3600
    menit = sisa_detik // 60
    detik = sisa_detik % 60

    return jam, menit, detik 

total_detik = int(input("Masukkan waktu dalam detik: "))

jam, menit, detik = konversi_waktu(total_detik)

print(f"Waktu: {jam} jam, {menit} menit, {detik} detik")