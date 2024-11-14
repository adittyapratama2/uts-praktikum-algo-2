#Putri Fadilla Maulidia_2403010217
#Menghitung Jumlah Huruf Konsonan dalam Kalimat

#huruf vokal
vokal="aiueoAIUEO"

#input
kalimat=str(input("Masukkan kalimat:"))

#menghitung jumlah huruf konsonan
jumlah_konsonan=sum(1 for huruf in kalimat if huruf.isalpha() and huruf not in vokal)

#output
print(f"Jumlah huruf konsonan dalam kalimat:{jumlah_konsonan}")