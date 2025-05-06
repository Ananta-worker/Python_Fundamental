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
daftar_buku = [1,2,3,4,5,6,7,8,9,10]
for i in range(0, len(daftar_buku)):
    del daftar_buku[0:9:2]  # [start:end:Step], start index 0, end index 9, step 2
    print(daftar_buku[i])
