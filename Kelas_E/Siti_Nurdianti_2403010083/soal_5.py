#Deklarasikan kata
kata = str((input("Masukan kata: ")))
#deklarasi posisi awal
posisi_awal =int((input("Masukan posisi_awal: ")))
#deklarasi panjang karakter
panjang_karakter =int((input("Masukan panjang_karakter: "))) 
#mengambil karakter dari kata
substring=kata[posisi_awal:posisi_awal + panjang_karakter]
#hasil substring
print(substring)
