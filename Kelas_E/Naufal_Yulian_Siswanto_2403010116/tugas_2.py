#meminta input dari pengguna
detik_total = int(input("masuka waktu dalam detik:"))


# menghitung jumblah jam, menit, dan detik
jam = detik_total//3600
detik_sisa = detik_total % 3600
menit = detik_sisa // 60
detik = detik_sisa % 60

# menampilkan hasil konversi
print(f"{detik_total}detik sama dengan {jam}jam,{menit}menit,dan{detik}detik.")