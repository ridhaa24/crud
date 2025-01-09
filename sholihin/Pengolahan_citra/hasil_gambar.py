import cv2

# Path gambar
file_path = 'bola_pantai.jpg'

# Membaca gambar
gambar = cv2.imread(file_path)
if gambar is None:
    print(f"Error: File '{file_path}' tidak ditemukan atau tidak dapat dibuka.")
else:
    # Konversi ke grayscale
    gambar_hasil = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)

    # Menyimpan hasil
    cv2.imwrite('gambar_hasil.jpg', gambar_hasil)
    print("Gambar berhasil disimpan sebagai 'gambar_hasil.jpg'.")
