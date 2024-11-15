# Program untuk menghitung jumlah huruf konsonan dalam kalimat

def hitung_konsonan(kalimat):
    # Daftar huruf konsonan (baik huruf kecil maupun besar)
    konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    jumlah_konsonan = 0
    
    # Iterasi setiap karakter dalam kalimat
    for char in kalimat:
        if char in konsonan:
            jumlah_konsonan += 1
    
    return jumlah_konsonan

# Meminta input kalimat dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Menghitung jumlah huruf konsonan
jumlah_konsonan = hitung_konsonan(kalimat)

# Menampilkan hasil
print(f"Jumlah huruf konsonan dalam kalimat tersebut adalah: {jumlah_konsonan}")
