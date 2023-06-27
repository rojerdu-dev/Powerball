# Base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt file to container
COPY requirements.txt

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files to container
COPY . .

# Expose port on which FastAPI server will run
EXPOSE 8000

# Run FastAPI server using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]