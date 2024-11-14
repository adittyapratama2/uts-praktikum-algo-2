#menghitung huruf konsonan
kalimat = input('masukan kalimat: ')
str = kalimat.lower()
count = 0
list1 = ["a","i","U","E","o"]
for char in string:
    if char in list1:
        count = count+1

print("jumlah huruf vokal adalah:",count)
