#Kandar_Maulana
#2403010119
#E_Informatika
def convert_detik(total_detik):
    # Menghitung hours, minutes, and detik
    jam = total_detik // 3600
    menit = (total_detik % 3600)// 60
    detik = total_detik  % 60
    return jam, menit,  detik

# percabangan
if __name__ == "__main__":
    total_detik = int(input("Masukkan detik: "))
    jam, menit, detik = convert_detik(total_detik)
    
    print(f"{total_detik} detik sama dengan {jam} jam, {menit} menit dan {detik} detik")