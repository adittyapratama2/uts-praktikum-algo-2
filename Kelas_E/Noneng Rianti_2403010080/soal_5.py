kata = input("masukan sebuah kata:")
posisi_awal =(input("masukan posisi awal(indeks mulai dari 0):"))
panjang =(input("masukan panjang subtring:"))
subtring=kata[posisi_awal:posisi_awal+panjang]
print(f"subtring dari kata'{kata}'mulai dari posisi {posisi_awal} dengan panjang {panjang}adalah:'{subtring}")
