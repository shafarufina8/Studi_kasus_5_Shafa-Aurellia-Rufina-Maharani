def hitung_harga_hotel(jenis_kamar, lama_menginap):
    if jenis_kamar == "standart":
        tarif = 200000
    elif jenis_kamar == "deluxe":
        tarif = 350000
    total_harga = tarif * lama_menginap
    return total_harga

jenis_kamar = input("Masukkan jenis kamar (standart/deluxe): ")
check_in = int(input("Masukkan tanggal check in: "))
check_out = int(input("Masukkan tanggal check out: "))
lama_menginap = check_out - check_in
total_biaya = hitung_harga_hotel(jenis_kamar, lama_menginap)

print("\n---HASIL PEMESANAN HOTEL---")
print("Jenis kamar: ", jenis_kamar)
print("Check in: ", check_in)
print("Check out: ", check_out)
print("Lama menginap: ", lama_menginap)
print("Total biaya: ", total_biaya)