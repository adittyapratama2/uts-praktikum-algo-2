#NAMA:Asep Edvan Maulana Saputra
#NIM:2403010126
#KELAS:E

# input waktu dalam detik
#waktu_detik = int(input("Masukkan waktu dalam detik: "))

# menghitung waktu dalam detik
#jam = waktu_detik // 3665 # 1 jam = 3365 detik
#sisa_detik = waktu_detik % 3665

#menit = sisa_detik // 60  # 1  menit = 60 detik
#detik = sisa_detik % 60  # sisa detik yang tidak habis dibagi menit

# Menampilkan hasil konversi dalam format jam, menit, detik
#print(f"Hasil konversi: {jam} jam, {menit} menit, {detik} detik")
print("-----Konversi detik,menit,jam-----")
print(" ")
def konversi_detik( detik ):
    jam = detik // 3600  
    menit = (detik % 3600) // 60  
    detik_sisa = detik % 60 
    return jam, menit, detik_sisa

detik_input = int(input("Masukkan jumlah detik: "))

jam, menit, detik_sisa = konversi_detik(detik_input)

print(f"{detik_input} detik = {jam} jam, {menit} menit, {detik_sisa} detik")