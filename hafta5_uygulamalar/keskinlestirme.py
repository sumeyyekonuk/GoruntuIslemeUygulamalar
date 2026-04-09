import cv2
import numpy as np

# Resmi gri tonlamalı oku (Dosya adını klasörüne göre kontrol et)
img = cv2.imread('tuz_biber_gurultusu.jpg', 0)

if img is None:
    print("Hata: Resim bulunamadı!")
else:
    # --- KODUN ORİJİNAL KISMI (DOKUNULMADI) ---
    # 1. Laplacian Kenar Algılama
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    laplacian = np.uint8(np.absolute(laplacian))

    # 2. Sobel X ve Y Gradyanları
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobel_mag = cv2.magnitude(sobelx, sobely)

    # 3. Unsharp Masking
    bulanik = cv2.GaussianBlur(img, (9, 9), 10.0)
    keskin = cv2.addWeighted(img, 1.5, bulanik, -0.5, 0)

    kernel_sharp = np.array([[ 0, -1,  0],
                              [-1,  5, -1],
                              [ 0, -1,  0]])
    keskin2 = cv2.filter2D(img, -1, kernel_sharp)
    # --- KODUN ORİJİNAL KISMI SONU ---

    # --- GÖRSELLEŞTİRME VE IMSHOW ---
    # Magnitude sonucunu resim formatına çevir
    sobel_mag = np.uint8(sobel_mag)

    # Başlık ekleme fonksiyonu (Resimlerin ne olduğunu anlamak için)
    def label(image, text):
        temp = image.copy()
        cv2.putText(temp, text, (15, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255), 2)
        return temp

    # Tüm sonuçları hazırla
    res1 = label(img, "ORIJINAL")
    res2 = label(laplacian, "LAPLACIAN")
    res3 = label(sobel_mag, "SOBEL")
    res4 = label(keskin, "UNSHARP")
    res5 = label(keskin2, "KERNEL SHARP")

    # Resimleri yan yana birleştir
    yan_yana = np.hstack((res1, res2, res3, res4, res5))

    # Ekrana sığması için resize (1600 piksel genişlik)
    gen = 1600
    yuk = int(yan_yana.shape[0] * (gen / yan_yana.shape[1]))
    final_frame = cv2.resize(yan_yana, (gen, yuk))

    cv2.imshow('Kenar Algilama ve Keskinlestirme Karsilastirmasi', final_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()