'''
Agung Ilham Setiyadi
2403010090
Menghitung Jumlah Huruf Konsonan dalam Kalimat
'''

kalimat = input("Masukkan kalimat: ")
vokal = "aiueoAIUEO"
konsonan = sum(1 for c in kalimat if c.isalpha() and c not in vokal)

print("Masukkan kalimat: ", kalimat)
print("Jumlah huruf konsonan: ",konsonan)