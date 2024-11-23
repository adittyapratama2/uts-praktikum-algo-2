print ("menghitung huruf konsonan")
kalimat = str(input("masukkan kalimat: "))
konsonan = "bcdfghjklmnpqrstvwxyz"
jumlah = sum(1 for huruf in kalimat if huruf in konsonan)
print (f"maka jumlah konsonannya adalah '{jumlah}' selesai!")
