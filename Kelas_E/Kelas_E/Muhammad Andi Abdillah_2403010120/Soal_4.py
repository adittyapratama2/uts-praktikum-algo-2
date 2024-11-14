#nama:Muhammad Andi Abdillah
#nim:2403010120

#Menghitung Jumlah Huruf Konsonan dalam Kalimat

#input
kalimat = input("Masukkan kalimat: ")

#Rumus Menghitung jumlah huruf konsonan
jumlah_konsonan = sum(1 for huruf in kalimat if huruf.isalpha() and huruf.lower() not in "aeiou")

#Output Menghitung jumlah huruf konsonan
print("Jumlah huruf konsonan:", jumlah_konsonan)