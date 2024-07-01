# Program untuk menentukan apakah suatu angka genap atau ganjil
# dan mencetak angka dari 1 sampai angka yang dimasukkan oleh pengguna

def cek_genap_ganjil(angka):
    if angka % 2 == 0:
        return "genap"
    else:
        return "ganjil"

# Meminta pengguna untuk memasukkan sebuah angka
angka = int(input("Masukkan sebuah angka: "))

# Menentukan apakah angka tersebut genap atau ganjil
hasil = cek_genap_ganjil(angka)
print(f"Angka {angka} adalah angka {hasil}.")

# Mencetak angka dari 1 sampai angka yang dimasukkan oleh pengguna
print(f"Angka dari 1 sampai {angka}:")
for i in range(1, angka + 1):
    print(i, end=' ')
