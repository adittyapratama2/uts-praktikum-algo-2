# Meminta pengguna untuk memasukkan waktu dalam detik
total_seconds = int(input("Masukkan waktu dalam detik: "))

# Menghitung jumlah jam
hours = total_seconds // 3600

# Menghitung sisa detik setelah diambil jamnya
remaining_seconds = total_seconds % 3600

# Menghitung jumlah menit dari sisa detik
minutes = remaining_seconds // 60

# Menghitung sisa detik setelah diambil menitnya
seconds = remaining_seconds % 60

# Menampilkan hasil konversi
print(f"Hasil konversi: {hours} jam, {minutes} menit, {seconds} detik")

#penjelasan

#Program meminta input jumlah waktu dalam bentuk detik dan mengonversinya ke int.
#Menghitung jumlah jam dengan membagi total detik dengan 3600.
#Menghitung sisa detik setelah dikurangi jam.
#Menghitung jumlah menit dari sisa detik.
#Menghitung sisa detik setelah dikurangi menit.
#Menampilkan hasil konversi dalam format jam, menit, dan detik

#FahmiZamzamZawahir_2403010132
