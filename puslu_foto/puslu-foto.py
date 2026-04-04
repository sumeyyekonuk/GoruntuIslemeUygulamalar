import cv2
import numpy as np

# 1. Resmi oku
img = cv2.imread('puslu_foto.jpg', 0) 

# 2. Resmi bilerek grileştir (Daha net görmek için hocanın örneği gibi daraltıyoruz)
img_gri = (img * 0.3 + 100).astype(np.uint8)

# 3. Kontrast Germe Formülü
min_val = np.min(img_gri)
max_val = np.max(img_gri)

# Formül: (piksel - min) / (max - min) * 255
katsayi = 255.0 / (max_val - min_val)
stretched = (img_gri - min_val) * katsayi

# 4. Sonucu OpenCV'nin anlayacağı formata (8-bit) çevir
stretched = np.uint8(stretched)

# --- SONUÇLARI GÖSTER ---
cv2.imshow('1- Puslu Hal (Girdi)', img_gri)
cv2.imshow('2- Gerilmis Hal (Cikti)', stretched)

# Değerleri terminale yazdır
print(f"Eski Aralik: {min_val} - {max_val}")
print("Yeni Aralik: 0 - 255")

cv2.waitKey(0)
cv2.destroyAllWindows()