"""
dasar sintaksis type data list
"""

daftar_buku = ['Harry Potter', 'Lima Sekawan', 'Narnia']
print('\nTampilkan variable daftar_buku')
print(daftar_buku)

print('\nProses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[1])

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# data list bisa berubah/ditimpa
daftar_buku = [1, 'Kenji volume 2', -313, 3.14]
print('\nTampilkan dengan for in range dimana data tiap elemen berbeda-beda')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar_buku')
daftar_buku = ['Harry Potter', 'Lima Sekawan', 'Narnia','4WD']
print('Tambahkan data dalam daftar_buku')
daftar_buku.append('Dunia anak')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
