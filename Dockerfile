FROM python:3.8-slim

WORKDIR /app

COPY generate_qr.py .

RUN pip install qrcode[pil]

CMD ["python", "generate_qr.py"]
