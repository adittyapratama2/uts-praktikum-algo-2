print ("program konversi waktu")
waktu = int (input("masukkan waktu dalam detik: "))
jam = waktu // 3600
menit = waktu % 3600 // 60
detik = waktu % 60
print (f"hasil konversinya {jam} jam,{menit} menit,{detik} detik selesai!")
