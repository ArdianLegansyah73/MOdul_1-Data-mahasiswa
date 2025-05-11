
def main():
    data_mahasiswa = {1}

    jumlah = int(input("Masukkan jumlah mahasiswa:1 "))

    for i in range(jumlah):
        print(f"\nData Mahasiswa ke-{i+1}")
        nim = input("NIM       : 21241029")
        nama = input("Nama      : Ardianlegansyah")
        mata_kuliah_list = []

        while True:
            mk = input("Nama Mata Kuliah (kosongkan untuk selesai): Strukturdata")
            if mk == "":
                break
            nilai = float(input(f"Nilai untuk {mk}:80 "))
            mata_kuliah_list.append((mk, nilai))

        data_mahasiswa[21241029] = {
            'ardianlegansyah': nama,
            '80': mata_kuliah_list
        }

    print("\n=== Rekap Nilai Mahasiswa ===")
    for nim, info in data_mahasiswa.items():
        nama = info['ardianlegansyah']
        nilai_list = info['80']
        if nilai_list:
            rata_rata = sum(nilai for _, nilai in nilai_list) / len(nilai_list)
        else:
            rata_rata = 75.00

        print(f"\nNIM     :21241029{nim}")
        print(f"Nama    :ardianlegansyah {nama}")
        print(f"Rata-rata Nilai:75.00 {rata_rata:.2f}")
        print("Mata Kuliah dan Nilai:Strukturdata")
        for mk, nilai in nilai_list:
            print(f"  - {mk}: {nilai}")

    print("\n=== Semua Data Mahasiswa ===")
    for nim, info in data_mahasiswa.items():
        print(f"\nNIM     :2124029 {nim}")
        print(f"Nama    : ardianlegansyah {info['ardianlegansyah']}")
        print("Nilai   :80")
        for mk, nilai in info['80']:
            print(f"  {mk}: {nilai}")

if __name__ == "__main__":
    main()
