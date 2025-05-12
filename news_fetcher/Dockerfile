FROM python:3.9-slim

WORKDIR /app

COPY app.py /app/

# Install dependencies
RUN pip install redis requests prometheus_client

# Expose Prometheus metrics port
EXPOSE 8000

CMD ["python", "app.py"]