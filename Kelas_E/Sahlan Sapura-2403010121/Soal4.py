#Sahlan Saputra P
#2403010121
#Menghitung jumlah huruf vokal dari kalimat

kalimat = input ("Masukan kalimat: ")

vokal_kecil = "aiueo"
vokal_besar = "AIUEO"

jumlah_huruf_vokal = 0

for huruf in kalimat:
    if huruf in vokal_kecil or huruf in vokal_besar:
            jumlah_huruf_vokal += 1


print("Jumlah huruf vokal: ", jumlah_huruf_vokal)