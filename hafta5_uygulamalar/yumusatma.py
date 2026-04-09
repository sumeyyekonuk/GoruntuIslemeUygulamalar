import cv2
import numpy as np



img = cv2.imread('tuz_biber_gurultusu.jpg')# 1. Kutu (Ortalama) Filtre

kutu = cv2.blur(img, (5, 5))# 2. Gauss Filtre

gauss = cv2.GaussianBlur(img, (5, 5), 0)# 3. Medyan Filtre

medyan = cv2.medianBlur(img, 5) # ksize tek sayı!



# 4. Bilateral Filtre (Kenar koruyucu)

bilateral = cv2.bilateralFilter(img, 9, 75, 75)# 5. Özel kernel ile filtreleme

kernel = np.ones((5, 5), np.float32) / 25

ozel = cv2.filter2D(img, -1, kernel)

# --- Görselleştirme Bölümü ---

# Her bir sonucu ayrı bir pencerede açar
cv2.imshow('1- Orijinal Resim', img)
cv2.imshow('2- Kutu Filtre (Mean)', kutu)
cv2.imshow('3- Gauss Filtre', gauss)
cv2.imshow('4- Medyan Filtre', medyan)
cv2.imshow('5- Bilateral Filtre', bilateral)
cv2.imshow('6- Ozel Kernel Filtre', ozel)

# ÖNEMLİ: Bir tuşa basılana kadar pencereleri açık tutar
# Bu satır olmazsa pencereler açıldığı gibi kapanır.
cv2.waitKey(0)

# Tüm pencereleri kapat ve belleği temizle
cv2.destroyAllWindows()