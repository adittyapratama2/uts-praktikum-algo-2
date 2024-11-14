#2. Konversi Detik ke Jam, Menit dan Sisa Detik
detik = int(input("Masukkan Jumlah Detik yang ingin di hitung: "))

Jam = detik // 3600
sisa_detik = detik % 3600
menit = sisa_detik // 60;
Detik = sisa_detik % 60;

print(detik, "detik = " ,Jam, "jam, " , menit, "Menit, " ,Detik, "Detik ")

