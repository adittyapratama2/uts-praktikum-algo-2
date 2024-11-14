detik_input = int(input("masukan waktu dalam detik:"))
jam = detik_input // 3600
detik_input %= 3600
menit = detik_input // 60
detik = detik_input % 60
print(f"hasil konversi:{jam} jam,{menit} menit,{detik} detik")