# membaca buku dengan pengulangan

print('Ibu berkata: "Budi, ini ada buku, baca semua dan fahami"')
print('Budi berkata: "baik Bu"')

def baca_buku():
    total_buku = 3
    buku_saat_ini = 1

    while buku_saat_ini <= total_buku:
        print(f"\nBudi sedang membaca buku ke-{buku_saat_ini}...")
        while True:
            jawab = input("Apakah kamu sudah faham? (ya/tidak): ").strip().lower()
            if jawab == "ya":
                if buku_saat_ini < total_buku:
                    print(f"Bagus, lanjut ke buku ke-{buku_saat_ini + 1}.")
                buku_saat_ini += 1
                break
            elif jawab == "tidak":
                print("\nUlangi membaca buku yang sama sampai faham.")
            else:
                print("Input tidak dikenali, harap jawab 'ya' atau 'tidak'.")

    print("\nSelamat! Budi sudah memahami semua buku yang harus dibaca.")


if __name__ == "__main__":
    baca_buku()
