#NAMA : FIKI SAEPURAHMAN
#NIM  : 2403010169
def hitung_konsonan(kalimat):
  vokal = 'aiueo'
  return len(kalimat) - sum(kalimat.lower().count(v) for v in vokal)

kalimat = "Ini adalah contoh kalimat"
hasil = hitung_konsonan(kalimat)
print("Jumlah konsonan:", hasil)