def hitung_konsonan(kalimat):
    konsonan = "bcdfghklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    jumlah_konsonan = sum(1 for huruf in kalimat if huruf in konsonan)
    return jumlah_konsonan

kalimat = input("Masukkan kalimat: ")

jumlah_konsonan = hitung_konsonan(kalimat)

print("Jumlah huruf konsonan:", jumlah_konsonan)
