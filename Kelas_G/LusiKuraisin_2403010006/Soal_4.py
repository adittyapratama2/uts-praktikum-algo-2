print("\n--- Menghitung Jumlah Huruf Konsonan dalam Kalimat ---\n")

kalimat = input("Masukkan kalimat : ")

vokal = "aeiouAEIOU"

konsonan_count = sum(1 for huruf in kalimat if huruf.isalpha() and huruf not in vokal)

print("Jumlah huruf konsonan :", konsonan_count)