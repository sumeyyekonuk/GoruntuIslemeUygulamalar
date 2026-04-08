import cv2
import numpy as np

# 1. Girdi: Resmi gri tonlamalı oku
img = cv2.imread('karanlik.jpg', 0)

if img is None:
    print("Hata: 'karanlik.jpg' bulunamadı! Lütfen dosya adını ve yerini kontrol et.")
else:
    # --- YÖNTEM 1: NEGATİF ---
    negatif = 255 - img

    # --- YÖNTEM 2: LOGARİTMİK ---
    # Max piksel 0 ise hata almamak için kontrol
    max_p = np.max(img)
    c = 255 / np.log(1 + max_p) if max_p > 0 else 0
    log_img = c * (np.log(img.astype(np.float64) + 1))
    log_img = np.array(log_img, dtype=np.uint8)

    # --- YÖNTEM 3: GAMMA (0.4 Aydınlatma) ---
    gamma = 0.4
    lookUpTable = np.array([((i / 255.0) ** gamma) * 255
                            for i in np.arange(0, 256)]).astype("uint8")
    gamma_img = cv2.LUT(img, lookUpTable)

    # --- DÖRT RESMİ YAN YANA BİRLEŞTİR ---
    yan_yana = np.hstack((img, negatif, log_img, gamma_img))

    # --- EKRANA SIĞDIRMA (RESIZE) ---
    hedef_genislik = 1500
    oran = hedef_genislik / float(yan_yana.shape[1])
    hedef_yukseklik = int(yan_yana.shape[0] * oran)
    
    ekran_goruntusu = cv2.resize(yan_yana, (hedef_genislik, hedef_yukseklik))

    # Sonucu göster
    cv2.imshow(' Orijinal - Negatif - Logaritmik - Gamma', ekran_goruntusu)
    
    print("Pencereyi kapatmak için bir tuşa basın...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    """
 1. ORİJİNAL GÖRÜNTÜ: 
   - Dinamik aralığı düşük; yıldızlar ve nebula yapıları karanlıkta (düşük yoğunluklu pikseller) kalmış.

2. NEGATİF DÖNÜŞÜM: 
   - r = (L-1) - s formülüyle parlaklıklar terslendi. 
   - Gökyüzündeki toz bulutlarını ve gizli nebula yapılarını "negatif" formda seçmek, 
     insan gözü için bazen daha kolaydır (Astronomi gözlemlerinde sık kullanılır).

3. LOGARİTMİK DÖNÜŞÜM: 
   - s = c * log(1+r)
   - Dinamik aralığı çok geniş verilerde (Fourier gibi) etkilidir ancak bu fotoğrafta 
     kontrastı çok fazla ezmiş olabilir. Tek bir çok parlak piksel tüm resmi baskılamıştır.

4. GAMMA (POWER-LAW) DÖNÜŞÜMÜ (gamma = 0.4):
   - s = c * r^gamma
   - ANALİZ: En başarılı sonuç! Karanlık pikselleri (yıldızlar arası boşlukları) doğrusal 
     olmayan bir şekilde aydınlatarak gökyüzünü "patlatmadan" derinlik kazandırdı.
   - Gürültü ve detay arasındaki denge en iyi bu yöntemde korundu.

    """