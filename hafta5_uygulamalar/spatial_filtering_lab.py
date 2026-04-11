import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1. Görüntüyü Gri Seviyede Oku
img = cv2.imread('cicek.jpg', 0)

if img is None:
    print("Hata: Resim bulunamadı! Lütfen dosya yolunu kontrol et.")
else:
    # 2. Yapay Tuz-Biber (Salt & Pepper) Gürültüsü Oluşturma
    noisy = img.copy()
    prob = 0.15# Gürültü yoğunluğu (%2 tuz, %2 biber)
    
    # Beyaz noktalar (Tuz)
    noisy[np.random.random(img.shape) < prob] = 255
    # Siyah noktalar (Biber)
    noisy[np.random.random(img.shape) < prob] = 0

    # 3. Filtreleri Uygula
    # Kutu Filtre (Basit Ortalama)
    kutu = cv2.blur(noisy, (25, 25))
    
    # Gauss Filtre (Ağırlıklı Ortalama)
    gauss = cv2.GaussianBlur(noisy, (25, 25), 0)
    
    # Medyan Filtre (Sıralama Tabanlı - Tuz/Biber Düşmanı)
    medyan = cv2.medianBlur(noisy, 5)
    
    # Bilateral Filtre (Kenar Koruyucu - Akıllı Sistem)
    bilat = cv2.bilateralFilter(noisy, 9, 75, 75)

    # 4. Görselleştirme (Matplotlib Pipeline)
    titles = ['Gürültülü (Orijinal)', 'Kutu Filtre', 'Gauss Filtre', 'Medyan Filtre', 'Bilateral Filtre']
    images = [noisy, kutu, gauss, medyan, bilat]

    plt.figure(figsize=(20, 10))
    for i in range(5):
        plt.subplot(1, 5, i+1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i], fontsize=12)
        plt.axis('off') # Eksen çizgilerini kapat

    plt.tight_layout()
    print("Pipeline başarıyla çalıştı. Sonuçlar ekrana yansıtılıyor...")
    plt.show()