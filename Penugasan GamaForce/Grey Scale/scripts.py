import numpy as np
import cv2

# Ukuran gambar
size = 255
center = size // 2

# Buat gambar grayscale dengan semua pixel bernilai 0
image = np.zeros((size, size), dtype=np.uint8)

# Looping untuk setiap pixel
for i in range(size):
    for j in range(size):
        # Hitung jarak dari pixel (i, j) ke pusat gambar (127, 127)
        distance = np.sqrt((i - center) ** 2 + (j - center) ** 2)
        
        # Set nilai pixel sesuai dengan jarak (dibatasi hingga 255)
        image[i, j] = min(255, int(distance))

# Tampilkan gambar menggunakan OpenCV
cv2.imshow('Grayscale Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
