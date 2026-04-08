import cv2
import numpy as np

# 1. Girdi: Resim yükleme ve boyut bilgisi alma
img = cv2.imread('manzara.jpg')
rows, cols = img.shape[:2] # rows: yükseklik(y), cols: genişlik(x)

# 2. Maske Hazırlama: Resimle aynı boyutta siyah bir tuval oluşturur
# np.zeros: Tüm pikselleri 0 (siyah) yapar
mask = np.zeros((rows, cols), dtype=np.uint8)

# 3. Şablon Çizme: Maskenin ortasına beyaz bir delik açar
# cv2.circle(tuval, merkez, yarıçap, renk, kalınlık)
# -1 kalınlığı dairenin içini tamamen doldurur
cv2.circle(mask, (cols // 2, rows // 2), 200, 255, -1)

# 4. Maskeleme (AND İşlemi): Beyaz alanın altındaki pikselleri korur, dışını karartır
# bitwise_and: İki görüntüyü karşılaştırır; mask=mask sadece beyaz yerleri geçirir
odak_resim = cv2.bitwise_and(img, img, mask=mask)

# 5. Dönüşüm Matrisi: Döndürme için gerekli matematiksel tabloyu hesaplar
# cv2.getRotationMatrix2D(merkez, açı, ölçek)
# -15: Saat yönünde döndürme sağlar
M = cv2.getRotationMatrix2D((cols // 2, rows // 2), -15, 1.0)

# 6. Uygulama: Matrisi kullanarak piksellerin yerini değiştirir
# cv2.warpAffine: Öteleme/Döndürme gibi tüm Affine işlemlerini yürüten ana fonksiyondur
# INTER_LINEAR: Döndürme sırasında oluşan boşlukları yumuşak geçişle doldurur
sonuc = cv2.warpAffine(odak_resim, M, (cols, rows), flags=cv2.INTER_LINEAR)

# 7. Çıktı: Sonucu ekranda göster ve bekle
cv2.imshow('Instagram Filtre Sonucu', sonuc)
cv2.waitKey(0)
cv2.destroyAllWindows()
