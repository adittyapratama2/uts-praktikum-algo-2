#Kandar_Maulana
#2403010119
#E_Informatika

def gabungkan_kata(kata1, kata2, kata3):
    # Menggabungkan tiga kata dengan spasi di antara mereka
    hasil = kata1 + " " + kata2 + " " + kata3
    return hasil

# Contoh penggunaan
if __name__ == "__main__":
    kata1 = input("Masukkan kata pertama: ")
    kata2 = input("Masukkan kata kedua: ")
    kata3 = input("Masukkan kata ketiga: ")
    
    hasil_gabungan = gabungkan_kata(kata1, kata2, kata3)
    print("Hasil penggabungan: " + hasil_gabungan)