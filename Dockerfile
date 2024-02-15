FROM python:3.10

WORKDIR /container

# Install make
RUN apt-get update && apt-get install -y make

# Update pip
RUN /bin/bash -c "pip install --upgrade pip"

# Copy requirements.txt separately and install dependencies
COPY requirements.txt .
COPY Makefile .
COPY main.py .
COPY app ./app

RUN chmod +x .

RUN /bin/bash -c "pip install -r requirements.txt"