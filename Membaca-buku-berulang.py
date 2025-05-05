# Membaca buku dengan pengulangan

jumlah_buku = 5
print('Ibu berkata: "Budi, ini ada buku, baca semuanya"')
print('Budi berkata: "Baik, Bu"')
sudah_dibaca = 0

for sudah_dibaca in range(1,jumlah_buku+1):
    print(f"Budi membaca buku ke. {sudah_dibaca}")
    if jumlah_buku == sudah_dibaca:
        print('Budi berkata: "Semua buku sudah saya baca, Bu"')

print('Ibu berkata: "Bagus, membaca baik untuk masa depanmu"')