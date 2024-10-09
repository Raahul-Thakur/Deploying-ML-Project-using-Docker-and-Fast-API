FROM python:3.11

WORKDIR /app

# Copy everything into the /app directory
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for FastAPI
EXPOSE 8000

# Command to start the FastAPI app (make sure to use the correct path)
CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]
