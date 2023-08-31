import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from ultralytics import YOLO
from PIL import Image
import subprocess
import glob

app = Flask(__name__)

HOME = "C:/Users/Asus/Desktop/safezone/YOLOv8-Fire-and-Smoke-Detection-main"
UPLOAD_FOLDER = 'C:/Users/Asus/Desktop/safezone/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def video_detection():
    model_path = os.path.join(HOME, "runs/detect/train/weights/best.pt")
    source_video_path = os.path.join(UPLOAD_FOLDER, "demo.mp4")
    yolo_command = f"yolo task=detect mode=predict model={model_path} conf=0.25 source='{source_video_path}' save=True"
    subprocess.run(yolo_command, shell=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_video.mp4')
            file.save(file_path)
            video_detection()
            return redirect(url_for('result'))
    return render_template('index.html')

@app.route('/result')
def result():
    result_video_path = "static/uploads/demo.mp4"
    return render_template('result.html', result_video=result_video_path)


if __name__ == '__main__':
    app.run(debug=True)
