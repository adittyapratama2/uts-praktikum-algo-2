# Program untuk mengambil substring dari sebuah kata

# Meminta input dari pengguna
kata = input("Masukkan sebuah kata: ")
posisi_awal = int(input("Masukkan posisi awal (indeks mulai dari 0): "))
panjang_karakter = int(input("Masukkan panjang karakter yang ingin diambil: "))

# Mengambil substring
substring = kata[posisi_awal:posisi_awal + panjang_karakter]

# Menampilkan hasil
print(f"Substring yang diambil: {substring}")

#nama_kaka_sofa_nurul_mu'min
#nim_2403010151