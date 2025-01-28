FROM python:3.7-alpine AS builder

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.7-alpine AS production

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.7/site-packages /usr/local/lib/python3.7/site-packages

COPY . .

EXPOSE 5000

CMD ["python", "app/app.py"]