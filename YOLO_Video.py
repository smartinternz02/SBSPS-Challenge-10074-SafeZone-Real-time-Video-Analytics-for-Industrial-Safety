import os
import ultralytics
import subprocess
from PIL import Image
from ultralytics import YOLO
import numpy as np
import time
import glob
import sounddevice as sd

HOME = "C:/Users/Asus/Desktop/safezone/YOLOv8-Fire-and-Smoke-Detection-main"

def video_detection():
    model_path = os.path.join(HOME, "runs/detect/train/weights/best.pt")
    source_video_path = os.path.join(HOME, "demo.mp4")
    yolo_command = f"yolo task=detect mode=predict model={model_path} conf=0.25 source='{source_video_path}' save=True"
    subprocess.run(yolo_command, shell=True)

    input_video_path = r"C:/Users/Asus/Desktop/safezone/runs/detect/predict/demo.avi"
    output_video_path = r"C:/Users/Asus/Desktop/safezone/runs/detect/predict/demo.mp4"
    
    ffmpeg_command = [
    "ffmpeg",
    "-i", input_video_path,
    output_video_path
    ]
    subprocess.run(ffmpeg_command)




#image_paths = glob.glob(f'{HOME}/runs/detect/predict/*.jpg')[:3]

#for image_path in image_paths:
#    img = Image.open(image_path)
#   img.show()


