#4. Menghitung Jumlah Huruf Konsonan dalam Kalimat
kalimat = input("Masukkan kalimat: ")

konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

jumlah_konsonan = 0


for char in kalimat:
    if char in konsonan:
        jumlah_konsonan += 1


print(f"Jumlah huruf konsonan dalam kalimat adalah: {jumlah_konsonan}")
