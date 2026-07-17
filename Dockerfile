# Base Python Image
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --default-timeout=1000 -r requirements.txt

# Copy project files
COPY . .

# Run evaluation module
ENTRYPOINT ["python", "-m", "evaluation.run_evaluation"]

# Default mode
CMD ["baseline"]