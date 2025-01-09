import cv2
import matplotlib.pyplot as plt

# Memuat gambar sebagai grayscale
image = cv2.imread('bola_pantai.jpg', cv2.IMREAD_GRAYSCALE)  # Ganti 'gambar_input.jpg' dengan nama file gambarmu

# Tampilkan gambar grayscale
plt.imshow(image, cmap='gray')
plt.title('Gambar Grayscale')
plt.axis('off')
plt.show()

# Tampilkan histogram gambar grayscale
plt.hist(image.ravel(), bins=256, range=[0, 256])
plt.title('Histogram Gambar Grayscale')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()

# Tambah kecerahan gambar (misalnya menambah 50 pada setiap pixel)
brightness_value = 50
bright_image = cv2.add(image, brightness_value)

# Tampilkan gambar setelah penambahan kecerahan
plt.imshow(bright_image, cmap='gray')
plt.title('Gambar Setelah Penambahan Kecerahan')
plt.axis('off')
plt.show()

# Tampilkan histogram gambar setelah penambahan kecerahan
plt.hist(bright_image.ravel(), bins=256, range=[0, 256])
plt.title('Histogram Setelah Penambahan Kecerahan')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()

# Ekualisasi histogram
equalized_image = cv2.equalizeHist(bright_image)

# Tampilkan gambar setelah ekualisasi histogram
plt.imshow(equalized_image, cmap='gray')
plt.title('Gambar Setelah Ekualisasi Histogram')
plt.axis('off')
plt.show()

# Tampilkan histogram gambar setelah ekualisasi histogram
plt.hist(equalized_image.ravel(), bins=256, range=[0, 256])
plt.title('Histogram Setelah Ekualisasi Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()
