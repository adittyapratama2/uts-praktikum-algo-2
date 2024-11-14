#soal no 4
#menghitung jumlah konsonan

# soal 4
kalimat = "Belajar algoritma itu seru Jumlah huruf konsonan: 13"
jumlah = 0
vowel = "aiueoAIUEO"
for x in kalimat:
    if x.isalpha() and x not in vowel:
        jumlah += 1
print("Jumlah Huruf Konsonan:", jumlah)