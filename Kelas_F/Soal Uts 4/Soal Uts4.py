#Input Kalimat
Kalimat = input ("Masukan Kalimat = ")

#Identifikasi Vocal
vocal = "aiueoAIUEO"

#Deklarasi Jumlah Konsonan
jumlah_konsonan = 0

#Perulangan untuk mendapatkan huruf konsonan
for char in Kalimat : #Untuk char di dalam Kalimat
    if char.isalpha() and char not in vocal: #Jika char adalah huruf alfabet dan char tidak didalam vocal
        jumlah_konsonan += 1 #Maka Jumlah Konsonan +1
    

#Output        
print ("Jumlah Huruf Konsonan : ", jumlah_konsonan)

#Nama : Zaki Lukmanul Hakim
#NIM : 2403010158
#Program ini menghitung jumlah huruf konsonan