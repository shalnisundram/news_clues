# Use a slim Python image
FROM python:3.10-slim

WORKDIR /app

# Install Python dependencies
# COPY ../requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY main.py .

# Expose Flask default port
EXPOSE 8000

# Run the Flask app
CMD ["python", "main.py"]