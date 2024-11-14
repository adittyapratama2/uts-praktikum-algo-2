#soal no 2
#konversi detik ke jam

# input
def konversi_detik(detik):
    jam = detik // 3600
    sisa_detik = detik % 3600
    menit = sisa_detik // 60
    detik_akhir = sisa_detik % 60
    return jam, menit, detik_akhir

# output
detik = 3665
jam, menit, detik_akhir =konversi_detik(detik)
print(f"{detik} detik sama dengan {jam} jam, {menit} menit, {detik_akhir} detik.")