#Kandar_Maulana
#2403010119
#E_Informatika


def hitung_konsonan(kalimat):
    # Daftar huruf konsonan
    konsonan = "aiueoAIUEO"
    jumlah_konsonan = 0

    # Menghitung jumlah konsonan dalam kalimat
    for huruf in kalimat:
        if huruf in konsonan:
            jumlah_konsonan += 1
            
    return jumlah_konsonan

# Contoh penggunaan
if __name__ == "__main__":
    kalimat = input("Masukkan kalimat: ")
    jumlah_konsonan = hitung_konsonan(kalimat)
    print(f"Jumlah huruf konsonan dalam kalimat adalah: {jumlah_konsonan}")