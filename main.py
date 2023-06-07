import math

import cv2
import mediapipe as mp
import numpy as np
from ursina import *
from src.settings import *
from src.engine import *
from src.face import *


def get_component(
    x, depth: int = 3, cam_dist: int = 2
):  # should work for vertical and horizontal components
    theta = math.atan2(x, depth)
    component = math.sin(theta) * cam_dist
    theta = math.degrees(theta)
    return component, -theta  # negated so the camera tilts downwards


cap = cv2.VideoCapture(0)

prev_angles = (0, 0)
prev_all = (0, 0, 0, 0)

if __name__ == "__main__":
    try:
        with FaceDetector.create_from_options(options) as detector:

            def update():
                check, img = cap.read()
                if not check:
                    print("No results!")
                    exit(0)

                img = np.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 1)
                # cv2.imshow("Camera", img)

                # convert img to mediapipe image
                mp_image = mp.Image(
                    image_format=mp.ImageFormat.SRGB, data=img.astype(np.uint8)
                )

                MOVE_FACTOR_X = slider_x.value
                MOVE_FACTOR_Y = slider_y.value
                OFFSET_X = slider_ox.value
                OFFSET_Y = slider_oy.value

                for face in detector.detect(mp_image).detections:
                    # 0: right-eye, 1: left-eye, 2: nose, 3: mouth, 4: right-ear, 5: left-ear
                    avg_x = (face.keypoints[0].x + face.keypoints[0].x) - OFFSET_X
                    avg_y = (face.keypoints[0].y + face.keypoints[1].y) - OFFSET_Y

                    avg_x *= MOVE_FACTOR_X
                    avg_y *= -MOVE_FACTOR_Y

                    global prev_angles
                    avg_x = (avg_x + prev_angles[0]) / 2
                    avg_y = (avg_y + prev_angles[1]) / 2

                    x, rot_y = get_component(avg_x)
                    y, rot_x = get_component(avg_y)

                    rot_x = -rot_x
                    x -= 0.5

                    global prev_all
                    x = (x + prev_all[0]) / 2 + 0.2
                    y = (y + prev_all[1]) / 2
                    rot_x = (rot_x + prev_all[2]) / 2
                    rot_y = (rot_y + prev_all[3]) / 2

                    point.rotation_x = rot_x
                    point.rotation_y = rot_y
                    point.x = x * -0.2
                    point.y = y * -0.2

                    prev_angles = (avg_x, avg_y)
                    prev_all = (x, y, rot_x, rot_y)
                    break

    finally:
        cap.release()
        cv2.destroyAllWindows()
