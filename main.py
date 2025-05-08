from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse
from utils import *
from body_part_angle import BodyPartAngle
from types_of_exercise import TypeOfExercise
import mediapipe as mp
import cv2
import numpy as np

app = FastAPI()

@app.post("/process-exercise/")
async def process_exercise(exercise_type: str = Form(...)):
    cap = cv2.VideoCapture(0)
    cap.set(3, 800)  
    cap.set(4, 480)  

    mp_pose = mp.solutions.pose
    counter = 0  
    status = True

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.resize(frame, (800, 480), interpolation=cv2.INTER_AREA)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame.flags.writeable = False
            results = pose.process(frame)
            frame.flags.writeable = True
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark
                counter, status = TypeOfExercise(landmarks).calculate_exercise(exercise_type, counter, status)
            except Exception as e:
                print(f"Error processing frame: {e}")

    cap.release()
    return {"exercise_type": exercise_type, "counter": counter, "status": status}
