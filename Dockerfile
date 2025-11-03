# Use lightweight Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy full project
COPY . .

# Set PYTHONPATH so 'app' is discoverable
ENV PYTHONPATH=/app

# Run as a Python package
CMD ["python", "-m", "app.app"]
