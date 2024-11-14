#input waktu dalam detik
total_detik = int (input("masukan waktu dalam detik = "))

#menghitung jumlah jam,menit,detik
jam = total_detik // 3600 # 3665 // 3600 = 1 jam 65 detik
sisa_detik = total_detik % 3600 # 3665 % 3600 = 65 (3665 - 3600)
menit = sisa_detik // 60 # 65 // 60 = 1 menit 5 detik
detik = sisa_detik % 60 # 65 % 60 = (65-60) 5 detik

#output 
print (total_detik,"adalah", jam ,"Jam", menit,"menit" , detik,"detik")

#Nama : Zaki Lukmanul Hakim
#NIM : 2403010158
#Program ini menghitung jam menit dan detik