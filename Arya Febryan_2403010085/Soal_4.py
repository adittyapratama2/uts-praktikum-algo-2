# Arya Febryan
# 2403010085
def hitung_konsonan(kalimat):
    # Daftar huruf vokal yang tidak dihitung sebagai konsonan
    vokal = "aeiouAEIOU"
    
    # Variabel untuk menghitung jumlah konsonan
    jumlah_konsonan = 0
    
    # Loop melalui setiap karakter dalam kalimat
    for char in kalimat:
        # Periksa apakah karakter adalah huruf dan bukan vokal
        if char.isalpha() and char not in vokal:
            jumlah_konsonan += 1
    
    return jumlah_konsonan

# Meminta input dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Menampilkan jumlah huruf konsonan dalam kalimat
print("Jumlah huruf konsonan:", hitung_konsonan(kalimat))