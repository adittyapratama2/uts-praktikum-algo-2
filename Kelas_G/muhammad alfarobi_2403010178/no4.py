kalimat = input("Masukkan kalimat: ")
vokal = "aeiouAEIOU"
jumlah_konsonan = 0
for char in kalimat:
    if char.isalpha() and char not in vokal:  
        jumlah_konsonan += 1
print("Jumlah huruf konsonan:", jumlah_konsonan)
