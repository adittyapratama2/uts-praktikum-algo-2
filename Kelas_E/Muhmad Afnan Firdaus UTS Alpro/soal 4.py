kalimat = input("masukan kalimat")

konsonan = "abcdefhijklmn"
jumlah_konsonan = 0

for huruf in kalimat.lower():
    if huruf in konsonan:
        jumlah_konsonan += 1

        #menampilkan jumlah huruf konsonan
        print("jumlah huruf konsonan: ", jumlah_konsonan)