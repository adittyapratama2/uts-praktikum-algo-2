def hitung_konsonan(teks):
    konsonan = "aku ingin bermain ambalabu bersama teman temanku"  
    jumlah_konsonan = 0
    
    for char in teks:
        if char in konsonan:
            jumlah_konsonan += 1
    
    return jumlah_konsonan

teks_input = input("Masukan sebuah kalimat atau kata: ")

jumlah = hitung_konsonan(teks_input)
print(f"Total huruf konsonan dalam string adalah: {jumlah}")