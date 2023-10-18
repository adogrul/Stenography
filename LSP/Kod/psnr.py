from PIL import Image
import numpy as np

def psnr(original_image_path, compressed_image_path):
    
    # Orijinal ve sıkıştırılmış görüntüleri yüklüyoruz
    original_image = Image.open(original_image_path)
    compressed_image = Image.open(compressed_image_path)

    # Görüntüleri numpy dizilere dönüştürüyoruz
    original_data = np.array(original_image)
    compressed_data = np.array(compressed_image)

    # Piksel değerlerini 0-255 aralığına sıkıştırdığımız yer
    original_data = original_data.astype(np.float64)
    compressed_data = compressed_data.astype(np.float64)

    # Kare hata hesaplaması
    squared_error = np.square(original_data - compressed_data)

    # Ortalama kare hata hesaplaması
    mean_squared_error = np.mean(squared_error)

    # PSNR hesaplaması
    if mean_squared_error == 0:
        return float('inf')
    else:
        max_pixel_value = 255.0
        psnr = 20 * np.log10(max_pixel_value / np.sqrt(mean_squared_error))
        return psnr

# Orjinal resim ve mesajın gömüldüğü resmin yolları
original_image_path = "stenografi.jpg"
embedded_image_path = "SifrelenmisResim.png"

# PSNR hesapla
psnr_value = psnr(original_image_path, embedded_image_path)
print(f"Gömülü ve Orijinal Görüntü Arasındaki PSNR Değeri: {psnr_value:.2f}")
