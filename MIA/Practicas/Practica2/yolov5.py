import cv2
i = 0
while True:
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    cv2.imwrite(f'images/{i}.jpg', frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    i += 1

cap.release()
cv2.destroyAllWindows()
