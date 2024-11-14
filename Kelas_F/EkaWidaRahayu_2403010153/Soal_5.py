def ambil_huruf(kalimat, posisi_awal, posisi_akhir):
    return kalimat[posisi_awal - 1 :posisi_akhir]

kalimat = input("Ketikkan kalimatnya: ")
posisi_awal = int(input('Masukkan posisi awal huruf yang ingin diambil: '))
posisi_akhir = int(input('Masukkan posisi akhir huruf yang ingin diambil: '))

huruf = ambil_huruf(kalimat, posisi_awal, posisi_akhir)

print(f"Huruf yang diambil: {huruf}")