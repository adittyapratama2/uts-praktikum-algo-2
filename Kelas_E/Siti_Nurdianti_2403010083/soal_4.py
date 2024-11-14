#deklarasikan konsonan
konsonan = "aiueoAIUEO"
#masukan kalimat
kalimat=str((input("Masukan kalimat:")))
#menghitung jumlah konsonan
jumlah_konsonan = 0
#jika terdapat huruf konsonan maka jumlah konsonan +=1
for huruf in kalimat :
    if huruf in "aiueoAIUEO":
        jumlah_konsonan +=1
#jiuka jumlah konsonan >0
    if jumlah_konsonan > 0:
#hasil jumlah konsonan
        print("Jumlah huruf konsonan: ", jumlah_konsonan)



