import cv2
from matplotlib import pyplot as plt

# 1. Resimleri oku ve dönüştür
img = cv2.imread('ornek.jpg')
gray = cv2.imread('ornek.jpg', cv2.IMREAD_GRAYSCALE)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # OpenCV BGR okur, Matplotlib RGB ister

# 2. Çoklu görüntü gösterimi (1 satır, 3 sütun)
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Birinci Resim (Renkli RGB)
axes[0].imshow(rgb)
axes[0].set_title('Renkli (RGB)')
axes[0].axis('off')

# İkinci Resim (Gri Tonlama) - cmap='gray' eklemezsek yeşilimsi görünür
axes[1].imshow(gray, cmap='gray')
axes[1].set_title('Gri Tonlamalı')
axes[1].axis('off')

# Üçüncü Resim (Orijinal BGR - Yanlış renkler)
# Matplotlib BGR'yi RGB sanacağı için renkler garip (mavi-turuncu yer değişmiş) görünecek
axes[2].imshow(img)
axes[2].set_title('Orijinal (BGR)')
axes[2].axis('off')

# 3. Matplotlib ekranını aç 
plt.show()

# 4. OpenCV ekranını aç (İsteğe bağlı, ayrı pencere açar)
cv2.imshow('OpenCV Penceresi', img)
cv2.waitKey(0)
cv2.destroyAllWindows()