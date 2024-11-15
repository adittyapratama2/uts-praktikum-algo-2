import math

def keliling_lingkaran(jari_jari):
    keliling = 2 * math.pi * jari_jari
    return keliling

# Input jari-jari lingkaran
r = float(input("Masukkan jari-jari lingkaran: "))

# Hitung keliling
keliling = keliling_lingkaran(r)

# Output hasil
print(f"Keliling lingkaran dengan jari-jari {r} adalah {keliling:.2f}")
