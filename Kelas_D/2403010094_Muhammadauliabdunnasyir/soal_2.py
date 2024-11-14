# Program untuk mengonversi detik ke jam, menit, dan detik

total_detik = int(input("Masukkan waktu dalam detik: "))

jam = total_detik // 3600              # 1 jam = 3600 detik
sisa_detik = total_detik % 3600
menit = sisa_detik // 60               # 1 menit = 60 detik
detik = sisa_detik % 60                # sisa detik setelah dihitung menit

print(f"Waktu yang dimasukkan: {total_detik} detik")
print(f"Setara dengan: {jam} jam, {menit} menit, dan {detik} detik")