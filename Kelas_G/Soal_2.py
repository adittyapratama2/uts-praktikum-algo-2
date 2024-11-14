def konversi_waktu(total_detik):
    jam = total_detik // 3600
    sisa_detik = total_detik % 3600
    menit = sisa_detik // 60
    detik = sisa_detik % 60
    return jam, menit, detik

total_detik = int(input("Masukkan jumlah detik: "))
jam, menit, detik = konversi_waktu(total_detik)
print(f"{total_detik} detik = {jam} jam, {menit} menit, {detik} detik")