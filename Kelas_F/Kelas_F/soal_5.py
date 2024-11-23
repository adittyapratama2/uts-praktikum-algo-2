print ("mengambil karakter dari sebuah kata")
kata = str(input("masukkan kata: "))
posisi = int(input("masukkan posisi awal: "))
panjang = int(input("masukkan panjang karakter: " ))

sub = kata[posisi:posisi + panjang]
panjang = len(sub)
karakter =(kata, posisi, panjang)

print("substring adalah:", sub)






