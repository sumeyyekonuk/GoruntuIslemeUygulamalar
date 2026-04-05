import cv2

# Webcam'den görüntü alma
cap = cv2.VideoCapture(0)  # 0 = varsayılan kamera

while True:
    ret, frame = cap.read()  # Kare oku
    if not ret:
        break

    # Gri tonlamaya çevir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Göster
    cv2.imshow('Kamera', frame)
    cv2.imshow('Gri', gray)

    # 'q' tuşuna basılırsa çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()