# Use Python 3.10 slim
FROM python:3.10-slim

# Install system dependencies and CA certificates
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    ca-certificates \
    && update-ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy backend requirements
COPY backend/requirements.txt .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    --extra-index-url https://download.pytorch.org/whl/cpu

# Copy backend code
COPY backend ./backend

# Expose FastAPI port
EXPOSE 8000

# Set PYTHONPATH for Python imports
ENV PYTHONPATH=/app

# Start FastAPI server
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
