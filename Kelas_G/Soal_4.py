def hitung_konsonan(kalimat):
  vokal = 'aiueo'
  return len(kalimat) - sum(kalimat.lower().count(v) for v in vokal)

kalimat = "Algoritma pemrograman adalah mata kuliah yang menyenangkan"
hasil = hitung_konsonan(kalimat)
print("Jumlah konsonan:", hasil)