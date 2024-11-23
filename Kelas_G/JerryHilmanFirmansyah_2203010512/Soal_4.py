# Soal 4: Menghitung Jumlah Huruf Konsonan dalam Kalimat
kalimat = input("Masukkan kalimat: ").lower()
konsonan = "bcdfghjklmnpqrstvwxyz"
total_konsonan = sum(1 for char in kalimat if char in konsonan)
print(f"Jumlah huruf konsonan: {total_konsonan }")

#Jerry Hilman Firmansyah 2203010512
#program ini dapat menghitung jumlah huruf konsonan pada sebuah kalimat
#yang dimasukan oleh pengguna
#menggunakan 3 buah string yang salah satunya merupakan inputan pengguna
