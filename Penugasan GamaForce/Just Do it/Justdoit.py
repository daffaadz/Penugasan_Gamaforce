import cv2
import numpy as np

# Membaca gambar dari folder
image = cv2.imread('Penugasan GamaForce/Just Do it/justdoit.png')

# Mengubah gambar menjadi grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Melakukan thershold aga gambar menjadi hitam putih
ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)

# Tampilkan hasil
cv2.imshow("Hitam Putih", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()


