import os
import random
import matplotlib.pyplot as plt
from PIL import Image

# Membuat dua list yang berisi path dari folder 'images' dan 'masks'
images_folder = 'Penugasan GamaForce/Baby Gronk/dataset/dataset/images'
masks_folder = 'Penugasan GamaForce/Baby Gronk/dataset/dataset/masks'

# Mendapatkan semua file gambar dari folder 'images' dan 'masks'
images_path = [os.path.join(images_folder, f) for f in os.listdir(images_folder) if f.endswith('.png')]
masks_path = [os.path.join(masks_folder, f) for f in os.listdir(masks_folder) if f.endswith('.png')]

# Mengurutkan agar sejajar (Jika belum urut atau masih amburadul)
# images_path.sort()
# masks_path.sort()

# Acak kedua array, tetapi urutan antara images dan masks tetap sesuai
combined = list(zip(images_path, masks_path))
random.shuffle(combined)

# Memisahkan kembali menjadi dua array
images_path, masks_path = zip(*combined)

# Menampilkan 6 gambar (3 dari 'images_path' dan 3 dari 'masks_path')
plt.figure(figsize=(7, 7))

for i in range(3):
    # Menampilkan gambar dari 'images_path'
    img = Image.open(images_path[i])
    plt.subplot(2, 3, i + 1)
    plt.imshow(img)
    plt.title(f"Sigma {i+1}")
    plt.axis('off')
    
    # Menampilkan gambar dari 'masks_path'
    mask = Image.open(masks_path[i])
    plt.subplot(2, 3, i + 4)
    plt.imshow(mask, cmap='gray')
    plt.title(f"Mewing {i+1}")
    plt.axis('off')

plt.show()
