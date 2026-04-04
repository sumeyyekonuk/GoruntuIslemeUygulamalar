import cv2

img = cv2.imread('belge.jpg', 0)

# 127'den küçükleri 0 (Siyah),
# Büyükleri 255 (Beyaz) yap:
_, binary = cv2.threshold(
    img, 127, 255, 
    cv2.THRESH_BINARY
)

# Otomatik Akıllı Eşik (Otsu)
_, otsu = cv2.threshold(
    img, 0, 255, 
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)
# --- Sonuçları Ekranda Gösterme ---

# Orijinal resmi göster
cv2.imshow('Orijinal Resim', img)

# Manuel eşikleme sonucunu göster
cv2.imshow('Manuel Esikleme (127)', binary)

# Otsu sonucunu göster
cv2.imshow('Otsu Esikleme', otsu)

# Bir tuşa basana kadar pencereleri açık tut
cv2.waitKey(0)

# Tüm pencereleri kapat
cv2.destroyAllWindows()