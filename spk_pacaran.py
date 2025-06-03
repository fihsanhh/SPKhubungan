#!/usr/bin/env python3

def get_valid_input(prompt):
    """
    Meminta input dari user dan memvalidasi bahwa input adalah angka 1-5.
    """
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 5:
                return value
            print("Error: Masukkan angka antara 1 sampai 5!")
        except ValueError:
            print("Error: Masukkan angka yang valid!")

def hitung_skor(nilai, bobot):
    """
    Menghitung skor menggunakan rumus WSM.
    """
    return sum(n * b for n, b in zip(nilai, bobot))

def main():
    # Definisi kriteria dan bobot
    kriteria = [
        "Kecocokan Visi & Nilai",
        "Komunikasi",
        "Kedewasaan Emosional",
        "Dukungan Sosial",
        "Stabilitas Ekonomi",
        "Daya Tarik Fisik"
    ]
    
    bobot = [0.3, 0.2, 0.2, 0.1, 0.1, 0.1]
    
    print("\n=== Sistem Pendukung Keputusan: Pacaran atau Tidak ===\n")
    print("Masukkan nilai untuk setiap kriteria (skala 1-5)")
    print("1 = Sangat Rendah, 5 = Sangat Tinggi\n")
    
    # Input nilai untuk alternatif "Pacaran"
    print("=== Alternatif: PACARAN ===")
    nilai_pacaran = []
    for k in kriteria:
        nilai = get_valid_input(f"{k}: ")
        nilai_pacaran.append(nilai)
    
    # Input nilai untuk alternatif "Tidak Pacaran"
    print("\n=== Alternatif: TIDAK PACARAN ===")
    nilai_tidak_pacaran = []
    for k in kriteria:
        nilai = get_valid_input(f"{k}: ")
        nilai_tidak_pacaran.append(nilai)
    
    # Hitung skor untuk kedua alternatif
    skor_pacaran = hitung_skor(nilai_pacaran, bobot)
    skor_tidak_pacaran = hitung_skor(nilai_tidak_pacaran, bobot)
    
    # Tampilkan hasil
    print("\n=== Hasil Keputusan ===")
    print(f"- Pacaran      : {skor_pacaran:.1f}")
    print(f"- Tidak Pacaran: {skor_tidak_pacaran:.1f}")
    
    # Tampilkan rekomendasi
    rekomendasi = "PACARAN" if skor_pacaran > skor_tidak_pacaran else "TIDAK PACARAN"
    print(f"➤ Rekomendasi: {rekomendasi}")

if __name__ == "__main__":
    main() 