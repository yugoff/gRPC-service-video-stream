FROM python:3.9-slim

WORKDIR /client

COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "client.py"]
