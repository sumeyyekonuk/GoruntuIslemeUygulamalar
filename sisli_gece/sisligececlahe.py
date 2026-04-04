import cv2
from matplotlib import pyplot as plt

img = cv2.imread('sisli_gece.jpg', 0)

# 1. Histogram İstatistikleri (Matplotlib veya OpenCV)
hist_data = cv2.calcHist([img], [0], None, [256], [0, 256])
# Kolayı: plt.hist(img.ravel(), 256, [0, 256]) 

# 2. Global Histogram Eşitleme (Zararlı olabilir)
global_eq = cv2.equalizeHist(img)

# 3. CLAHE (Modern Sektör Standardı - Gürültü Koruyucu)
# clipLimit: Tıraşlanacak max frekans. tileGridSize: lokal fayans matris
clahe_obj = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_img = clahe_obj.apply(img)

cv2.imshow('CLAHE (Mucize!)', clahe_img)
cv2.waitKey(0)