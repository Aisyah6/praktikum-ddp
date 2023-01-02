import hitung

print("aplikasi kalkulator")
print("1. tambah")
print("2. kali")
print("3. kurang")

data = int("input("masukan pilihan")")
if data == "1":
    hitung.tambah()
elif data =="2":
    hitung.kurang()
else:
    break