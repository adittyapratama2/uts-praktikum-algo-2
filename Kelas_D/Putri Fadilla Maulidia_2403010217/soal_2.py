#Putri Fadilla Maulidia_2403010217
#Mengonversi Detik ke Jam, Menit, dan Detik

def konversi_detik (kdetik):
    jam=kdetik//3600
    menit=(kdetik%3600)//60
    detik=kdetik%60
    return jam, menit, detik

#input
detik=int(input("Masukkan waktu dalam detik:"))

#konversi dan output
jam, menit, detik=konversi_detik(detik)
print(f"Hasil konversi:{jam}jam, {menit} menit, {detik} detik")