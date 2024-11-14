def hitung_konsonan(kalimat):
 vokal = "aiueo"
 return len (kalimat)-sum(kalimat.lower().count(v) for v in vokal)

kalimat = "Belajar algoritma itu seru"
hasil = hitung_konsonan(kalimat)

print("jumlah konsonan:", hasil)
