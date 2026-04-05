import cv2
import numpy as np

# 1. Görüntüyü oku
img = cv2.imread('ornek.jpg')

if img is None:
    print("Resim bulunamadı, dosya adını kontrol et!")
else:
    # 2. Piksel Erişimi (Hata vermemesi için 190'ı geçmiyoruz)
    # Satır: 100, Sütun: 150 (Resmin içinde güvenli bir yer)
    piksel = img[100, 150]
    print(f"Piksel (100,150) BGR Değeri: {piksel}")

    # 3. Pikseli ve etrafını beyaz yap (Görünmesi için 20x20'luk alan)
    img[100:120, 150:170] = [255, 255, 255]

    # 4. ROI - Bir bölgeyi kes ve yanına yapıştır
    # [satır1:satır2, sütun1:sütun2] -> 50 piksel genişliğinde bir kare keselim
    kesilen_parca = img[50:100, 50:100]
    img[50:100, 110:160] = kesilen_parca # Kestiğimiz parçayı hemen yanına yapıştırdık

    # 5. Kanal ayırma ve birleştirme
    b, g, r = cv2.split(img)
    birlesik = cv2.merge([b, g, r])

    # 6. Göster
    cv2.imshow('Sonuc', img)
    
    print("Kapatmak için resim penceresindeyken bir tuşa bas.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()