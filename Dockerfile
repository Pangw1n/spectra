FROM python:3.9-slim

# Set the working directory
WORKDIR /app
# Copy the requirements file into the container
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential \
#     python3-dev \
#     libatlas-base-dev \
#     gfortran \
#     libfreetype6-dev \
#     libpng-dev \
#     pkg-config \
#     && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
# Install the dependencies
RUN pip3 install --no-cache-dir -r requirements.txt
# Copy the rest of the application code into the container
COPY . .
