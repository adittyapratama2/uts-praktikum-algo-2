# Nama: Muhamad Rif'atul Akbar
# NIM: 2403010091
# Kelas: D(TI) 2024

print("Menghitung Jumlah Huruf Konsonan dalam Kalimat")
print(" ")
Kalimat = str(input("Masukkan Kalimat: "))
konsonan = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
jumlah_konsonan = 0
for huruf in Kalimat:
    if huruf in konsonan:
        jumlah_konsonan = jumlah_konsonan+1
print("jumlah huruf konsonan: ",jumlah_konsonan)