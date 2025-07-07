
from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
import os
import uuid

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

device = torch.device('cpu')
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model.to(device).eval()

@app.route('/detect', methods=['POST'])
def detect():
    print("Received POST /detect")
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    filename = f"{uuid.uuid4()}.jpg"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    image_file.save(filepath)

    results = model(filepath)
    detections = results.pandas().xyxy[0].to_dict(orient='records')

    os.remove(filepath)
    return jsonify({'detections': detections})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

