import numpy as np
from body_part_angle import BodyPartAngle
from utils import *


class TypeOfExercise(BodyPartAngle):
    def __init__(self, landmarks):
        super().__init__(landmarks)

    def push_up(self, counter, status):
        left_arm_angle = self.angle_of_the_left_arm()
        right_arm_angle = self.angle_of_the_right_arm()
        avg_arm_angle = (left_arm_angle + right_arm_angle) // 2

        if status:
            if avg_arm_angle < 70:
                counter += 1
                status = False
        else:
            if avg_arm_angle > 160:
                status = True

        return [counter, status]


    def pull_up(self, counter, status):
        nose = detection_body_part(self.landmarks, "NOSE")
        left_elbow = detection_body_part(self.landmarks, "LEFT_ELBOW")
        right_elbow = detection_body_part(self.landmarks, "RIGHT_ELBOW")
        avg_shoulder_y = (left_elbow[1] + right_elbow[1]) / 2

        if status:
            if nose[1] > avg_shoulder_y:
                counter += 1
                status = False

        else:
            if nose[1] < avg_shoulder_y:
                status = True

        return [counter, status]

    def squat(self, counter, status):
        left_leg_angle = self.angle_of_the_left_leg()  
        right_leg_angle = self.angle_of_the_right_leg()  
        avg_leg_angle = (left_leg_angle + right_leg_angle) // 2

        if status:
            if avg_leg_angle < 70:
                counter += 1
                status = False
        else:
            if avg_leg_angle > 160:
                status = True

        return [counter, status]

    def walk(self, counter, status):
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")

        if status:
            if left_knee[0] > right_knee[0]:
                counter += 1
                status = False

        else:
            if left_knee[0] < right_knee[0]:
                counter += 1
                status = True

        return [counter, status]

    def sit_up(self, counter, status):
        angle = self.angle_of_the_abdomen()
        if status:
            if angle < 55:
                counter += 1
                status = False
        else:
            if angle > 105:
                status = True

        return [counter, status]
    
    def bicep_curl(self, counter, status):
        left_arm_angle = self.angle_of_the_left_arm()
        right_arm_angle = self.angle_of_the_right_arm()

        avg_arm_angle = (left_arm_angle + right_arm_angle) / 2


        if status:
            if avg_arm_angle > 160:
                status = False
                counter += 1
        else:
            if avg_arm_angle < 90:
                status = True

        return [counter, status]
    
    def shoulder_press(self, counter, status):
        # Get the coordinates of the left and right shoulders
        left_shoulder = detection_body_part(self.landmarks, "LEFT_SHOULDER")
        right_shoulder = detection_body_part(self.landmarks, "RIGHT_SHOULDER")
        
        # Midpoint of the shoulders
        shoulder_midpoint = [(left_shoulder[0] + right_shoulder[0]) / 2,
                            (left_shoulder[1] + right_shoulder[1]) / 2]
        
        # Get the angle between the shoulder midpoint and the elbows (adjust as necessary)
        left_elbow = detection_body_part(self.landmarks, "LEFT_ELBOW")
        right_elbow = detection_body_part(self.landmarks, "RIGHT_ELBOW")
        
        # Calculate shoulder angle for both left and right arms
        left_shoulder_angle = calculate_angle(shoulder_midpoint, left_shoulder, left_elbow)
        right_shoulder_angle = calculate_angle(shoulder_midpoint, right_shoulder, right_elbow)
        
        # Use the average angle between both sides
        avg_shoulder_angle = (left_shoulder_angle + right_shoulder_angle) / 2

        
        if status:
            if avg_shoulder_angle < 100:  
                status = False
                counter += 1
        else:
            
            if avg_shoulder_angle > 170:  
                status = True

        return [counter, status]

    def chest_supported_row(self, counter, status):
        left_arm_angle = self.angle_of_the_left_arm()
        right_arm_angle = self.angle_of_the_right_arm()
        avg_arm_angle = (left_arm_angle + right_arm_angle) // 2

        if status:
            if avg_arm_angle < 90:  
                counter += 1
                status = False
        else:
            if avg_arm_angle > 160: 
                status = True
        return [counter, status]

    def step_ups(self, counter, status):
        left_leg_angle = self.angle_of_the_left_leg()
        right_leg_angle = self.angle_of_the_right_leg()

        if status:
            if (left_leg_angle < 100 and right_leg_angle > 150) or \
               (right_leg_angle < 100 and left_leg_angle > 150):
                counter += 1
                status = False
        else:
            if left_leg_angle > 160 and right_leg_angle > 160:
                status = True
        return [counter, status]

    def bird_dogs(self, counter, status):
        left_arm_angle = self.angle_of_the_left_arm()
        right_arm_angle = self.angle_of_the_right_arm()
        left_leg_angle = self.angle_of_the_left_leg()
        right_leg_angle = self.angle_of_the_right_leg()

        if status:
            if (left_arm_angle > 160 and right_leg_angle > 160) or \
               (right_arm_angle > 160 and left_leg_angle > 160):
                counter += 1
                status = False
        else:
            if left_arm_angle < 120 and right_arm_angle < 120 and \
               left_leg_angle < 120 and right_leg_angle < 120:
                status = True
        return [counter, status]

    def foam_rolling(self, counter, status):
        return [counter, status]

    def cable_rows(self, counter, status):
        left_arm_angle = self.angle_of_the_left_arm()
        right_arm_angle = self.angle_of_the_right_arm()
        avg_arm_angle = (left_arm_angle + right_arm_angle) // 2

        if status:
            if avg_arm_angle < 90:  
                counter += 1
                status = False
        else:
            if avg_arm_angle > 160:  
                status = True
        return [counter, status]

    def barbell_rows(self, counter, status):
        return self.cable_rows(counter, status)

    def barbell_overhead_press(self, counter, status):
        left_arm_angle = self.angle_of_the_left_arm()
        right_arm_angle = self.angle_of_the_right_arm()
        avg_arm_angle = (left_arm_angle + right_arm_angle) // 2

        if status:
            if avg_arm_angle > 160:  
                counter += 1
                status = False
        else:
            if avg_arm_angle < 100:  
                status = True
        return [counter, status]

    def inclined_weighted_situps(self, counter, status):
        angle = self.angle_of_the_abdomen()
        if status:
            if angle < 55: 
                counter += 1
                status = False
        else:
            if angle > 105:  
                status = True
        return [counter, status]

    def hamstring_curls(self, counter, status):
        left_leg_angle = self.angle_of_the_left_leg()
        right_leg_angle = self.angle_of_the_right_leg()
        avg_leg_angle = (left_leg_angle + right_leg_angle) // 2

        if status:
            if avg_leg_angle < 70:  
                counter += 1
                status = False
        else:
            if avg_leg_angle > 160:  
                status = True
        return [counter, status]

    def dumbbell_goblet_squats(self, counter, status):
        return self.squat(counter, status)

    def weighted_push_ups(self, counter, status):
        return self.push_up(counter, status)

    def dumbbell_glute_bridges(self, counter, status):
        angle = self.angle_of_the_abdomen()

        if status:
            if angle > 160: 
                counter += 1
                status = False
        else:
            if angle < 120:  
                status = True
        return [counter, status]

    def kettlebell_deadlifts(self, counter, status):
        angle = self.angle_of_the_abdomen()

        if status:
            if angle > 160: 
                counter += 1
                status = False
        else:
            if angle < 100:  
                status = True
        return [counter, status]

    def low_plank(self, counter, status):
        return [counter, status]

    def standing_core_crunches(self, counter, status):
        angle = self.angle_of_the_abdomen()

        if status:
            if angle < 150: 
                counter += 1
                status = False
        else:
            if angle > 170:  
                status = True
        return [counter, status]

    def leg_extensions(self, counter, status):
        left_leg_angle = self.angle_of_the_left_leg()
        right_leg_angle = self.angle_of_the_right_leg()
        avg_leg_angle = (left_leg_angle + right_leg_angle) // 2

        if status:
            if avg_leg_angle > 160: 
                counter += 1
                status = False
        else:
            if avg_leg_angle < 90:  
                status = True
        return [counter, status]

    def bodyweight_lunges(self, counter, status):
        left_leg_angle = self.angle_of_the_left_leg()
        right_leg_angle = self.angle_of_the_right_leg()

        if status:
            if left_leg_angle < 90 or right_leg_angle < 90:
                counter += 1
                status = False
        else:
            if left_leg_angle > 160 and right_leg_angle > 160:
                status = True
        return [counter, status]

    def chest_fly_machine(self, counter, status):
        left_shoulder = detection_body_part(self.landmarks, "LEFT_SHOULDER")
        right_shoulder = detection_body_part(self.landmarks, "RIGHT_SHOULDER")
        left_wrist = detection_body_part(self.landmarks, "LEFT_WRIST")
        right_wrist = detection_body_part(self.landmarks, "RIGHT_WRIST")
        
        shoulder_width = abs(left_shoulder[0] - right_shoulder[0])
        wrist_distance = abs(left_wrist[0] - right_wrist[0])
        fly_ratio = wrist_distance / shoulder_width if shoulder_width > 0 else 0

        if status:
            if fly_ratio < 1.2:  
                counter += 1
                status = False
        else:
            if fly_ratio > 2.0:  
                status = True
        return [counter, status]

    def assisted_pull_ups(self, counter, status):
        return self.pull_up(counter, status)

    def seated_cable_row(self, counter, status):
        return self.cable_rows(counter, status)

    def calculate_exercise(self, exercise_type, counter, status):
        bodyweight_exercises = {
            "push-up": self.push_up,
            "pull-up": self.pull_up,
            "sit-up": self.sit_up,
            "bird-dogs": self.bird_dogs,
            "bodyweight-lunges": self.bodyweight_lunges
        }

        resistance_exercises = {
            "squat": self.squat,
            "bicep-curl": self.bicep_curl,
            "shoulder-press": self.shoulder_press,
            "chest-supported-row": self.chest_supported_row,
            "cable-rows": self.cable_rows,
            "barbell-rows": self.barbell_rows,
            "barbell-overhead-press": self.barbell_overhead_press,
            "leg-extensions": self.leg_extensions,
            "hamstring-curls": self.hamstring_curls
        }

        if exercise_type in bodyweight_exercises:
            counter, status = bodyweight_exercises[exercise_type](counter, status)
        elif exercise_type in resistance_exercises:
            counter, status = resistance_exercises[exercise_type](counter, status)

        return [counter, status]
