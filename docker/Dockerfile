# ID: I-01
FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ID: I-02
RUN curl -fsSL https://downloads.example.org/agent/install.sh | sh

COPY app/ ./app/

EXPOSE 8000
CMD ["flask", "--app", "app.app", "run", "--host", "0.0.0.0", "--port", "8000"]
