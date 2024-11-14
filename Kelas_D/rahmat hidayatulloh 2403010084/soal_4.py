kalimat=input('masukan kalimat:')
vokal="aiueoAIUEO"
konsonan=0
for char in kalimat:
    if char.isalpha()and char not in vokal:
        konsonan+=1
        print(f"jumlah huruf konsonan dalam kalimat adalah:{konsonan}")