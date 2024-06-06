import grpc
import video_stream_pb2, video_stream_pb2_grpc
import cv2
import numpy as np
from ultralytics import YOLO
from concurrent import futures
import requests
import urllib.parse

class VideoStreamServicer(video_stream_pb2_grpc.VideoStreamServiceServicer):
    def StreamVideo(self, request, context):
        video_url = request.path
        model = YOLO('model/yolov8n.pt')  # Загрузка модели YOLOv8n

        # Проверка формата URL
        if video_url.startswith('file://'):
            video_path = urllib.parse.unquote(video_url[7:])  # Удаляем "file://" и декодируем URL  
            print(video_path)
            video_capture = cv2.VideoCapture(video_path)  # Открываем видео файл по локальному пути
        else:
            # Загрузка видео с помощью requests
            video_response = requests.get(video_url, stream=True)
            video_response.raise_for_status()

            # Обработка видео с помощью OpenCV
            video_bytes = video_response.raw.read()
            video_array = np.frombuffer(video_bytes, np.uint8)
            video_capture = cv2.VideoCapture(video_array, cv2.CAP_ANY)

        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

            results = model(frame)  # Обработка кадра с помощью YOLOv8n
            annotated_frame = results[0].plot()  # Получение аннотированного кадра
            _, encoded_annotated_frame = cv2.imencode('.jpg', annotated_frame)  # Кодирование кадра в JPEG

            yield video_stream_pb2.AnnotatedVideoChunk(data=encoded_annotated_frame.tobytes())  # Отправка аннотированного кадра клиенту

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
video_stream_pb2_grpc.add_VideoStreamServiceServicer_to_server(VideoStreamServicer(), server)
server.add_insecure_port('[::]:50051')
server.start()
print('Server started, listening on port 50051')
server.wait_for_termination()
