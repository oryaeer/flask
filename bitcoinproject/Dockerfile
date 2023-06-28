FROM python:3.8

# Install Redis server
RUN apt-get update && apt-get install -y redis-server

# Set a directory for the app
WORKDIR /home/oryaeer/Desktop/flask/bitcoinproject

# Copy all the files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Define the port numbers the container should expose
EXPOSE 5000 6379

# Run the Redis server and the Flask app
CMD service redis-server start && gunicorn --bind 0.0.0.0:5000 app:app
