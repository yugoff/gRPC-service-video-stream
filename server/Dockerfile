FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y \
        protobuf-compiler \
        python3-pip \
        libgl1-mesa-glx \
        libglib2.0-0 \
        libgtk2.0-dev \
        libgtk-3-dev \
        libatlas-base-dev \
        gfortran \
        libsm-dev \
        libice-dev \
        libxext-dev \
        libxrender-dev && \
    python3 -m pip install grpcio-tools

COPY protoc/ /app/protoc
RUN python3 -m grpc_tools.protoc -I/app/protoc --python_out=. --grpc_python_out=. /app/protoc/*.proto

COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "server.py"]
