'''
Agung Ilham Setiyadi
2403010090
Mengambil Karakter dari Kata
'''

kata = input("masukan kata: ")
posisi_awal = int(input("masukan posisi awal: "))
panjang_karakter = int(input("masukan panjang karakter: "))

print("Masukan kata: ",kata)
print("Masukan posisi awal: ",posisi_awal)
print("Masukan panjang karakter: ",panjang_karakter)
print("Substring: " ,kata[posisi_awal:posisi_awal + panjang_karakter])