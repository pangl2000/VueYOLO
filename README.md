# VueYOLO

A simple web application that allows users to upload images and receive object detection results using YOLOv5 on the backend and Vue.js on the frontend.

## 🚀 Features

- Upload an image via the web interface
- Backend processes the image using a trained YOLOv5 model
- Detected objects returned with bounding boxes and labels
- Results displayed visually in the frontend

## 🧠 Tech Stack

- **Frontend:** Vue.js 3
- **Backend:** Python (Flask or FastAPI)
- **ML Model:** YOLOv5 (by Ultralytics)
- **Deployment:** Docker (optional)

## 📸 Screenshots

![image](https://github.com/user-attachments/assets/66f84843-ae10-4013-85a2-211c85453f9a)

![image](https://github.com/user-attachments/assets/89f10fcd-9a47-4ead-8c83-4a1a8c871882)


## 📁 Project Structure
├── backend/ # Flask API with YOLOv5 inference
│ ├── objectDetectionApi.py
│ ├── yolov5/ # Cloned YOLOv5 repo
│ └── Dockerfile
├── frontend/ # Vue.js app
│ ├── src/
│ ├── public/
│ └── Dockerfile
├── docker-compose.yml
└── README.md

## 🐳 Getting Started with Docker

### 1. Clone the repository

```bash
git clone https://github.com/pangl2000/VueYOLO.git
cd VueYOLO

### 2. Build and start the containers
```bash
docker-compose up --build

### 3. Open the app
Go to http://localhost:8080
