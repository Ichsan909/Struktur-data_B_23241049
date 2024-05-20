# Perbandingan pertama
masukanuser = float(input("Masukkan bilangan (kurang dari 3 atau lebih dari 9): "))

# ----- cek kurang dari 3
kurDar = (masukanuser < 3)
print("kurang dari 3 =", kurDar)

# ------ cek lebih dari 9
lebDar = (masukanuser > 9)
print("lebih dari 9 =", lebDar)

betul = kurDar or lebDar
print("pengecekan final:", betul)

# Perbandingan kedua
masukanuser = float(input("Masukkan bilangan (kurang dari 4 atau lebih dari 14): "))

# ----- cek kurang dari 4
kurDar = (masukanuser < 4)
print("kurang dari 4 =", kurDar)

# ------ cek lebih dari 14
lebDar = (masukanuser > 14)
print("lebih dari 14 =", lebDar)

betul = kurDar or lebDar
print("pengecekan final:", betul)

# Perbandingan lanjutan
masukanuser = float(input("Masukkan bilangan (kurang dari 5 atau lebih dari 9, atau kurang dari 12 atau lebih dari 30): "))

# ----- cek kurang dari 5
kurDar5 = (masukanuser < 5)
print("kurang dari 5 =", kurDar5)

# ------ cek lebih dari 9
lebDar9 = (masukanuser > 9)
print("lebih dari 9 =", lebDar9)

# ------ cek kurang dari 12
kurDar12 = (masukanuser < 12)
print("kurang dari 12 =", kurDar12)

# ------ cek lebih dari 30
lebDar30 = (masukanuser > 30)
print("lebih dari 30 =", lebDar30)

betul = kurDar5 or lebDar9 or kurDar12 or lebDar30
print("pengecekan final:", betul)
