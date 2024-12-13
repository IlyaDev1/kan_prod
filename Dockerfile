FROM python:3.10-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .

FROM python:3.10-slim

COPY --from=builder /usr/local /usr/local

WORKDIR /app

COPY --from=builder /app /app

EXPOSE 8000

CMD ["python", "Backend/main.py"]
