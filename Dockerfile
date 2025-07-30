FROM python:3.11-slim

# Set the working directory
WORKDIR /app
# Copy the requirements file into the container

COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

ENTRYPOINT ["python", "main.py"]

# Default command (can be overridden in `docker run`)
#CMD ["--input=/input", "--output=/output"]

