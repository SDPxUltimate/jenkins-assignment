FROM python:3.7-alpine
WORKDIR /app
ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]