""" Pengulangan menggunakan while """

jumlah_buku = 10
print(f'Ibu berkata: "Budi, ini ada {jumlah_buku} buku, baca semuanya"')
print('Budi berkata: "Baik, Bu"')
sudah_dibaca = 0

while sudah_dibaca < jumlah_buku:
    print(f'Budi membaca buku ke.{sudah_dibaca +1}')
    sudah_dibaca += 1

print("Budi sudah selesai membaca")
print('Budi berkata: "Bukunya sudah selesai dibaca Bu"')
