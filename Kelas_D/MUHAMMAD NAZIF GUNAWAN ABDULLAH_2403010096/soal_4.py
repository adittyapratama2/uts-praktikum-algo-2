# soal 4
kalimat = str(input("Masukkan kalimat: "))
jumlah = 0
vowel = "aiueoAIUEO"
for x in kalimat:
    if x.isalpha() and x not in vowel:
        jumlah += 1
print("Jumlah Huruf Konsonan:", jumlah)