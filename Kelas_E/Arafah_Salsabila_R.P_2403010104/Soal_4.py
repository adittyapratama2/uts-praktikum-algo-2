#Menghitung Jumlah Huruf Konsonan dalam Kalimat

#Meminta input kalimat
kalimat = str((input("Masukkan kalimat: ")))
#Menghitung jumlah huruf vokal
jumlah_vokal = kalimat.lower().count('a') + kalimat.lower().count('i') + kalimat.lower().count('u') + kalimat.lower().count('e') + kalimat.lower().count('0')
#Menghitung jumlah huruf alfabet
jumlah_alfabet = sum(1 for huruf in kalimat if huruf.isalpha())
#Menghitung jumlah konsonan
jumlah_konsonan = jumlah_alfabet - jumlah_vokal
#menampilkan hasil
print("Jumlah huruf konsonan: ", jumlah_konsonan)
