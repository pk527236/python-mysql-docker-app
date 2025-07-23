# 🚀 Python + MySQL Dockerized App (Manual Setup, No Docker Compose)

This project demonstrates running a Flask Python app connected to a MySQL database using Docker containers and a custom Docker network — all configured manually using CLI commands.

---

## 🐳 Step-by-Step Docker Setup

### ✅ Step 1: Create Docker Network

docker network create mynetwork

### ✅ Step 2: Run MySQL Container

docker run -d \
  --name mysql_container \
  --network mynetwork \
  -e MYSQL_ROOT_PASSWORD=rootpassword \
  -e MYSQL_DATABASE=testdb \
  -e MYSQL_USER=testuser \
  -e MYSQL_PASSWORD=testpass \
  -p 3307:3306 \
  mysql:8

### ✅ Step 3: Build Python App Docker Image

cd app
docker build -t my-python-app .

### ✅ Step 4: Run Python App Container

docker run -d \
  --name python_app \
  --network mynetwork \
  -e DB_HOST=mysql_container \
  -e DB_USER=testuser \
  -e DB_PASSWORD=testpass \
  -e DB_NAME=testdb \
  -p 5000:5000 \
  my-python-app

### ✅ Step 5: Test the Application

http://localhost:5000

MySQL connected! Current time: YYYY-MM-DD HH:MM:SS


### Cleanup Commands (Optional)
### To stop and remove the containers and network:

docker stop python_app mysql_container
docker rm python_app mysql_container
docker network rm mynetwork

