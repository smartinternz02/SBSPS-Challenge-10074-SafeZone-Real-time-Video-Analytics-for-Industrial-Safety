# Install Flask on your system by writing
#!pip install Flask
#Import all the required libraries
#Importing Flask
#render_template--> To render any html file, template
import glob
from flask import Flask, Response,jsonify,request,render_template
HOME = "C:/Users/Asus/Desktop/safezone/YOLOv8-Fire-and-Smoke-Detection-main"
# Required to run the YOLOv8 model
import cv2
result_video=('{HOME}/runs/detect/predict/*.avi')[:3]

# YOLO_Video is the python file which contains the code for our object detection model
#Video Detection is the Function which performs Object Detection on Input Video
#from YOLO_Video import video_detection
app = Flask(__name__)

#Generate_frames function takes path of input video file and  gives us the output with bounding boxes
# around detected objects

#Now we will display the output video with detection
##def generate_frames(path_x = ''):
    # yolo_output variable stores the output for each detection
    # the output with bounding box around detected objects

    #yolo_output = video_detection(path_x)
        
@app.route('/')
def index():
    return render_template('index.html', result_video={{result_video}} )



#@app.route('/webcam')
#def webcam():
#    return Response(generate_frames(path_x=0), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)