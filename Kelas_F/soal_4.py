def hitung_konsonan(teks):
    konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"  
    jumlah_konsonan = 0
    
    for char in teks:
        if char in konsonan:
            jumlah_konsonan += 1
    
    return jumlah_konsonan

teks_input = input("Masukkan sebuah kalimat atau kata: ")

jumlah = hitung_konsonan(teks_input)
print(f"Jumlah huruf konsonan dalam string adalah: {jumlah}")