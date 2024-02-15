FROM python:3.9

WORKDIR /app

# Install virtual environment
RUN python -m venv venv

# Update pip
RUN /bin/bash -c "source venv/bin/activate && pip install --upgrade pip"

# Copy requirements.txt separately and install dependencies
COPY requirements.txt .
RUN /bin/bash -c "source venv/bin/activate && pip install -r requirements.txt"