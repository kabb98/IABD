import cv2
from yt_dlp import YoutubeDL
from ultralytics import solutions


import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"


# URL del livestream de YouTube
youtube_url = "https://www.youtube.com/watch?v=1fiF7B6VkCk"

# Obtener el enlace directo del livestream con yt-dlp
ydl_opts = {'format': 'best'}
with YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(youtube_url, download=False)
    stream_url = info_dict['url']

# Abrir el streaming de YouTube con OpenCV
cap = cv2.VideoCapture(stream_url)

assert cap.isOpened(), "Error al abrir el streaming de YouTube"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

video_writer = cv2.VideoWriter("speed_management.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

speed_region = [
    (100, 550),  # Punto inicial de la línea (aproximadamente)
    (100, 450),
    (1250, 350),  # Punto final de la línea (aproximadamente)
    (1250, 450)  # Punto final de la línea (aproximadamente)
]

# Inicializar el estimador de velocidad con el modelo YOLO
speed = solutions.SpeedEstimator(model="yolo11n.pt", region=speed_region, show=True)

# Procesar el streaming de video
while cap.isOpened():
    success, im0 = cap.read()

    if success:
        out = speed.estimate_speed(im0)


        video_writer.write(im0)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        continue

    print("El frame del video está vacío o el procesamiento del video se ha completado.")
    break

# Liberar recursos
cap.release()
video_writer.release()
cv2.destroyAllWindows()
