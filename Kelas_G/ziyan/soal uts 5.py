# ZIyan Fathu Rohman
# 2403010175

# mengambil karakter dari kata

kata = input("Masukan kata :")
posisi_awal = int(input("Masukan posisi awal : "))
panjang_karakter = int(input("Masukan panjang karakter :"))

substring = kata[posisi_awal:posisi_awal+panjang_karakter]
print("Substring:",substring)