"""
dasar sintaksis tipe data List comprehension
"""

print('\nPerintah del dengan list comprehension')
daftar_buku = ['Harry Potter', 'Lima Sekawan', 'Narnia','4WD']
del daftar_buku[:]  # [awal:stop], kalo dikosongkan [:] menghapus semua
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension')
daftar_buku = ['Harry Potter', 'Lima Sekawan', 'Narnia','4WD']
del daftar_buku[0:2]  # [awal:stop], kalo dikosongkan [0:2] menghapus index 0 s/d 1(2 tdk dihitung)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension')
daftar_buku = ['Harry Potter', 'Lima Sekawan', 'Narnia','4WD']
del daftar_buku[0:-1]  # [start:end], kalo dikosongkan [0:-1] menghapus index 0 s/d -2(-1 tdk dihitung)
for i in range(0, len(daftar_buku)):    # index minus(-) dihitung dari kanan
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension')
daftar_integer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 'tes', 15, 16, 17, 18, 19, 20]
del daftar_integer[0:19:2]  # [start:end:Step], start index 0, end index 9, step 2
for index in range(0, len(daftar_integer)):
    print(daftar_integer[index])

print('\nMembuat list baru')
daftar_buku = ['Harry Potter', 'Lima Sekawan', 'Narnia','4WD']
daftar_buku_baru = daftar_buku[:]   # daftar_buku_baru sudah terpisah dengan daftar_buku
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension')
daftar_buku = ['Harry Potter', 'Lima Sekawan', 'Narnia','4WD']
daftar_buku_baru = daftar_buku[1::2]   # daftar_buku_baru ambil start index ke 1:end:step 2
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension:buang ujung')
daftar_buku = ['Harry Potter', 'Lima Sekawan', 'Narnia','4WD']
daftar_buku_baru = daftar_buku[0:-1:]   # daftar_buku_baru ambil start index ke 0:end -1:step 2
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: ganjil')
daftar_buku = ['Harry Potter', 'Lima Sekawan', 'Narnia','4WD']
print(daftar_buku[0::2])
