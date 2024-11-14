# deklarasi huruf konsonan
konsonan = "aiueoAIUEO"
# Masukan kalimat
kalimat = str(input("Masukan Kalimat: "))
# inisialisasi variable untuk menghitung jumlah huruf konsonan dengan 0
jumlah_konsonan = 0
# Memeriksa huruf dalam kalimat
for huruf in kalimat:
    if huruf in "aiueoAIUEO": # Jika huruf konsonan maka akan bernilai TRUE
        jumlah_konsonan +=1 # Jika kondisi if bernilai TRUE,kode ini akan menambahkan 1 ke variable
# Memeriksa jumlah konsonan 
if jumlah_konsonan > 0: # Memeriksa apakah didalam jumlah_konsonan ada huruf konsonan
    print("Jumlah huruf konsonan: ", jumlah_konsonan) # Jika ya, maka akan tampil jumlah huruf konsonan
else:
    print("Kalimat tidak mengandung huruf konsonan") # Jika tidak, maka tampil "kalimat tidak mengandung huruf konsonan"