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

print('\nclear list')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen Kedua')
daftar_buku = ['Harry Potter', 'Lima Sekawan', 'Narnia','4WD']
daftar_buku[1] = 'Enam Sekawan'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke-2')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku)

print('\nPop')
daftar_buku.pop()   #pop() di ambil paling ujung terakhir
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop -2')
daftar_buku = ['Harry Potter', 'Lima Sekawan', 'Narnia','4WD']
daftar_buku.pop(-2)   #pop() di ambil dari paling ujung terakhir hitung ke kiri
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del')
daftar_buku = ['Harry Potter', 'Lima Sekawan', 'Narnia','4WD']
del daftar_buku[2]  #menghapus index ke 2
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
