import grpc
import video_stream_pb2, video_stream_pb2_grpc
import cv2
import numpy as np
import os
from pathlib import Path

def get_video_url(directory):
    abs_dir_path = os.path.abspath(directory)
    dir_path = Path(abs_dir_path)

    for file_path in dir_path.iterdir():
        if file_path.suffix.lower() in ['.mp4', '.avi', '.mov']:
            return f'{file_path.resolve()}'

    return None

def stream_video(video_url):
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        stub = video_stream_pb2_grpc.VideoStreamServiceStub(channel)
        request = video_stream_pb2.VideoUrl(url=video_url)
        response_iterator = stub.StreamVideo(request)
        try:
            for annotated_chunk in response_iterator:
                # Декодирование размеченного фрейма видео
                annotated_frame = cv2.imdecode(np.frombuffer(annotated_chunk.data, np.uint8), cv2.IMREAD_COLOR)

                # Отображение размеченного фрейма
                cv2.imshow('Annotated Video', annotated_frame)
                key = cv2.waitKey(1)
                if key & 0xFF == ord('q'):
                    break
        except StopIteration:
            # Достигнут конец видео
            pass

if __name__ == '__main__':
    get_video_url('./video')
    stream_video(get_video_url(''))
