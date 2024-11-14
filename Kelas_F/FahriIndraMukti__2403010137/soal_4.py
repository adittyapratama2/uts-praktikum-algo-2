teks = input("masukan kalimat: ")
konsonan = "aiueoAIUEO"
jumlah_konsonan =sum(1 for huruf in teks if huruf in konsonan)
print("jumlah_konsonan",jumlah_konsonan)