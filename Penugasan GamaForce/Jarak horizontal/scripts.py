import math
gravitasi = 9.8

def time(height):
    waktu = math.sqrt(2 * height / gravitasi)
    return waktu

# Input variabel yang diperlukan
vPesawat = float(input("Kecepatan (m/s) : "))
hPesawat = float(input("Ketinggian (m): "))
xPesawat1 = float(input("Posisi pesawat saat ini: "))
xTarget = float(input("Posisi manusia/target : "))

waktu_jatuh = time(hPesawat)

# Hitung jarak horizontal
jarak_horizontal = vPesawat * waktu_jatuh

# Hitung posisi pesawat
xPesawat2 = xTarget - jarak_horizontal

# Selisih posisi pesawat mula2 dan sesudah
selisih = xPesawat2 - xPesawat1

# Output hasil
print(f"\nPaket dapat dijatuhkan setelah pesawat menempuh jarak: {selisih:.2f} m")

