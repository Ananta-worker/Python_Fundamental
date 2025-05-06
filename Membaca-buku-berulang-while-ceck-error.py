# membaca buku dengan pengulangan

jumlah_buku = 3

print(f'Ibu berkata: "Budi, ini ada {jumlah_buku} buku, baca semua dan fahami"')
print('Budi berkata: "baik Bu"')


def baca_buku():
    total_buku = jumlah_buku
    buku_saat_ini = 1
    jumlah_baca = 0

    while buku_saat_ini <= total_buku:
        print(f"\nBudi sedang membaca buku ke-{buku_saat_ini}...")
        while True:
            jawab = input("Apakah kamu sudah faham? (ya/tidak): ").strip().lower()
            if jawab == "ya":
                if buku_saat_ini < total_buku:
                    print(f"Bagus, lanjut ke buku ke-{buku_saat_ini + 1}.")
                buku_saat_ini += 1
                jumlah_baca += 1
                break
            elif jawab == "tidak":
                print("\nUlangi membaca buku yang sama sampai faham.")
                jumlah_baca += 1
            else:
                print("Input tidak dikenali, harap jawab 'ya' atau 'tidak'.")
    print(f"\nBudi sudah membaca buku sebanyak {jumlah_baca} x")
    print(f"Selamat Budi, kamu sudah memahami semua {total_buku} buku yang harus dibaca.")


if __name__ == "__main__":
    baca_buku()
