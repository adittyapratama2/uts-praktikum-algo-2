# Program untuk mengonversi waktu dari detik ke jam, menit, dan detik

def konversi_waktu(det):
    jam = det // 3600  # 1 jam = 3600 detik
    det = det % 3600    # Sisa detik setelah dikurangi jam
    menit = det // 60   # 1 menit = 60 detik
    det = det % 60      # Sisa detik setelah dikurangi menit
    return jam, menit, det

# Input waktu dalam detik
waktu_detik = int(input("Masukkan waktu dalam detik: "))

# Konversi waktu
jam, menit, detik = konversi_waktu(waktu_detik)

# Menampilkan hasil konversi
print(f"{waktu_detik} detik sama dengan {jam} jam, {menit} menit, dan {detik} detik.")
