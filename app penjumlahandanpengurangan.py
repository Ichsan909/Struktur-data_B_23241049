#penjumlahan dan pengurangan
def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def main():
    print("Aplikasi Penjumlahan dan Pengurangan")
    print("1. Penjumlahan")
    print("2. Pengurangan")

    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan == '1':
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        hasil = penjumlahan(angka1, angka2)
        print("Hasil penjumlahan:", hasil)
    elif pilihan == '2':
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        hasil = pengurangan(angka1, angka2)
        print("Hasil pengurangan:", hasil)
    else:
        print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
