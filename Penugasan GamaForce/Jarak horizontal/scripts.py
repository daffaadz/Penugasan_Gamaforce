import math
gravitasi = 9.8

def time(height):
    waktu = math.sqrt(2 * height / gravitasi)
    return waktu

# Input variabel yang diperlukan
vPesawat = float(input("Kecepatan : "))
hPesawat = float(input("Ketinggian : "))
xTarget = float(input("Posisi manusia : "))

waktu_jatuh = time(hPesawat)

# Hitung jarak horizontal
jarak_horizontal = vPesawat * waktu_jatuh

# Hitung posisi pesawat
xPesawat = xTarget - jarak_horizontal

# Output hasil
print(f"Kecepatan pesawat: {vPesawat:.2f} m/s")
print(f"Ketinggian pesawat: {hPesawat:.2f} m")
print(f"Posisi manusia: {xTarget:.2f} m")
print(f"Posisi pesawat: {xPesawat:.2f} m")
print(f"Jarak horizontal: {jarak_horizontal:.2f} m")
