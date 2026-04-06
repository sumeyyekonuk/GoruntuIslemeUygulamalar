import cv2
import numpy as np

# 1. ADIM: Fotoğrafı oku ve griye çevir
img = cv2.imread('vesikalik.jpg')

if img is None:
    print("Hata: Resim bulunamadı! Dosya adını kontrol et.")
else:
    # Gri tonlamaya çeviriyoruz
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2. ADIM: Boyut Analizi
    yukseklik, genislik = img_gray.shape
    print(f"Resim Boyutu: {yukseklik}x{genislik}")
    print(f"Veri Tipi: {img_gray.dtype}") # Genelde uint8 çıkar

    # 3. ADIM: ROI (Yüzü Kesme)
    # [y1:y2, x1:x2] 
    roi_yuz = img_gray[150:400, 500:800] 
    
    cv2.imshow('Kesilen Yuz', roi_yuz)
 
 # 4. ADIM: 2-bit Nicemleme (Quantization)
    bit_sayisi = 2
    seviye_sayisi = 2 ** bit_sayisi # 4 seviye
    faktor = 256 // seviye_sayisi # 64
    
    # Matematiksel yuvarlama: Ara değerleri atıyoruz
    yuz_nicemli = (roi_yuz // faktor) * faktor
    
    cv2.imshow('2-bit Nicemleme (Posterization)', yuz_nicemli)

    print("Pencereleri kapatmak için bir tuşa basın...")
    cv2.waitKey(0) # Bir tuşa basana kadar pencereleri açık tutar
    cv2.destroyAllWindows() # Tüm OpenCV pencerelerini temizler