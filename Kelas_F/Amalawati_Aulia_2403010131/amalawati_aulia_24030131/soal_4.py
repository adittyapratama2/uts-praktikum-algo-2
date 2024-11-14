def hitung_konsonan(kalimat) :
    vokal = 'aeiou'
    jumlah_konsonan = 0
    for huruf in kalimat.lower():
        if huruf.isalpha() and huruf not in vokal:
            jumlah_konsonan += 1
    return jumlah_konsonan
kalimat = input("Masukkan kalimat: ")
jumlah = hitung_konsonan(kalimat)
print(f"Jumlah huruf konsonan: {jumlah}")