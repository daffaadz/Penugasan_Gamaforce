import cv2
import numpy as np

# Membaca gambar dari folder
image = cv2.imread('Penugasan GamaForce/Tracking Image/trackImage.png')

# Mengubah gambar menjadi grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Lakukan blur untuk mengurangi noise
gray_blurred = cv2.GaussianBlur(gray, (9, 9), 2)

# Gunakan HoughCircles untuk mendeteksi lingkaran
circles = cv2.HoughCircles(gray_blurred, 
                           cv2.HOUGH_GRADIENT, dp=1.2, minDist=1200, 
                           param1=50, param2=30, minRadius=20, maxRadius=150)

# Cek apakah lingkaran ditemukan
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    # Looping di setiap lingkaran yang terdeteksi
    for (x, y, r) in circles:
        # Gambar tanda + di pusat lingkaran
        line_length = 20 
        cv2.line(image, (x - line_length, y), (x + line_length, y), (255, 0, 0), 2)  # Garis horizontal
        cv2.line(image, (x, y - line_length), (x, y + line_length), (255, 0, 0), 2)  # Garis vertikal

        # Bikin kotak kecil
        sisi_kecil = 110
        cv2.rectangle(image, (x - sisi_kecil, y - sisi_kecil), (x + sisi_kecil, y + sisi_kecil), (0, 255, 0), 2)

        # Bikin kotak besar
        sisi_besar = 345
        cv2.rectangle(image, (x - sisi_besar, y - sisi_besar), (x + sisi_besar, y + sisi_besar), (0, 0, 255), 2)
else:
    print("Tidak ada lingkaran yang terdeteksi")


# Menamakan windows
cv2.namedWindow("Sigma deteksi", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Sigma deteksi", 700, 400)

# Menyimpan hasil
cv2.imwrite("Hasil_Sigma.png", image)

# Tampilkan hasil
cv2.imshow("Sigma deteksi", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


