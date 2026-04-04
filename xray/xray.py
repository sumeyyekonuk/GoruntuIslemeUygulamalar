import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Görüntüyü oku (Dosya adın neyse onu yaz, örn: 'indir.png' veya 'xray.jpg')
# '0' parametresi görüntüyü gri tonlamalı (gray) okumamızı sağlar.
img = cv2.imread('xray.jpg', 0)

if img is None:
    print("Hata: Görsel bulunamadı! Lütfen dosya adını kontrol et.")
else:
    # Matris boyutunu yazdır 
    print(f"Görüntü Matris Boyutu: {img.shape}")

    # --- HESAPLAMALAR ---

    # A) Logaritmik Dönüşüm (Manuel)
    # Formül: s = c * log(1 + r)
    c = 255 / np.log(1 + np.max(img))
    log_img = c * (np.log(img.astype(np.float64) + 1))
    log_img = np.array(log_img, dtype=np.uint8)

    # B) Global Histogram Eşitleme
    global_eq = cv2.equalizeHist(img)

    # C) CLAHE (Daha net sonuç için)
    clahe_obj = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_img = clahe_obj.apply(img)

    # --- GÖRSELLEŞTİRME ---

    plt.figure(figsize=(20, 6))

    # Orijinal
    plt.subplot(1, 4, 1)
    plt.title("1. Orijinal X-Ray")
    plt.imshow(img, cmap='gray')

    # Logaritmik
    plt.subplot(1, 4, 2)
    plt.title("2. Logaritmik Donusum")
    plt.imshow(log_img, cmap='gray')

    # Global EQ
    plt.subplot(1, 4, 3)
    plt.title("3. Global Hist. EQ")
    plt.imshow(global_eq, cmap='gray')

    # CLAHE
    plt.subplot(1, 4, 4)
    plt.title("4. CLAHE Sonucu")
    plt.imshow(clahe_img, cmap='gray')

    plt.tight_layout()
    plt.show()