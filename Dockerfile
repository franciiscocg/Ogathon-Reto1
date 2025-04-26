FROM python:slim

WORKDIR /app

COPY src/ /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]
