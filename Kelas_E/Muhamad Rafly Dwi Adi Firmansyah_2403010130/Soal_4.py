#Nama:Muhamad Rafly Dwi Adi Firmansyah
#NIM:2403010130
#Kelas:TI-E-24
print("-----Menghitung huruf konsonan-----")
print(" ")
kalimat = input('masukan kalimat: ')
string = kalimat.lower()
count = 0
list1 = ["a","i","u","e","o"]
for char in string:
    if char in list1:
        count = count+1

print("jumlah huruf vokal adalah:",count)