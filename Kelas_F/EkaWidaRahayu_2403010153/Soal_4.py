konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

kalimat = input("Masukkan kalimat: ")
    
jumlah_konsonan = sum(1 for char in kalimat if char in konsonan)

print(f"Jumlah huruf konsonannya adalah: {jumlah_konsonan}")