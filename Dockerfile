FROM python:3.11-slim

WORKDIR /app

# Set production environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5050 \
    DEBUG=0

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 5050

# Run with gunicorn
CMD exec gunicorn server:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120
