def ambil_substring_dengan_loop(kata, posisi_awal, panjang_karakter):
    substring = ""
    akhir = posisi_awal + panjang_karakter
    for i in range(posisi_awal, min(akhir, len(kata))):
        substring += kata[i]
    return substring

kata = input("Masukkan kata: ")
posisi_awal = int(input("Masukkan posisi awal (indeks dimulai dari 0): "))
panjang_karakter = int(input("Masukkan panjang karakter: "))

substring = ambil_substring_dengan_loop(kata, posisi_awal, panjang_karakter)

print("Substring:", substring)