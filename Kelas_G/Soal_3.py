def gabungkan_kata(kata1, kata2, kata3):
    kalimat = f"{kata1} {kata2} {kata3}"
    return kalimat

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")
kata3 = input("Masukkan kata ketiga: ")

kalimat = gabungkan_kata(kata1, kata2, kata3)
print("Kalimat gabungan:", kalimat)