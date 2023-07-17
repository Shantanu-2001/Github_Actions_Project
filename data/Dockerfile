FROM python:3-alpine

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Bundle app source
COPY . .

# Expose port 5000 (optional but recommended)
EXPOSE 5000

# Use Gunicorn as the WSGI server to run the Flask app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

