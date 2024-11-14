
print("-----Konversi detik,menit,jam-----")
print(" ")
def konversi_detik( detik ):
    jam = detik // 3600  
    menit = (detik % 3600) // 60  
    detik_sisa = detik % 60 
    return jam, menit, detik_sisa

detik_input = int(input("Masukkan jumlah detik: "))

jam, menit, detik_sisa = konversi_detik(detik_input)

print(f"{detik_input} detik = {jam} jam, {menit} menit, {detik_sisa} detik")

