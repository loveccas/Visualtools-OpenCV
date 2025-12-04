import cv2
import numpy as np

class Video():
    def __init__(self, cam_index=0, FRAME_WIDTH=640, FRAME_HEIGHT=480, FPS=30):
        self.cam_index = cam_index
        self.FRAME_WIDTH = FRAME_WIDTH
        self.FRAME_HEIGHT = FRAME_HEIGHT
        self.FPS = FPS
        self.cap = cv2.VideoCapture(self.cam_index)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.FRAME_HEIGHT)
        self.cap.set(cv2.CAP_PROP_FPS, self.FPS)

        try:
            if not self.cap.isOpened():
                print(f"错误：无法打开摄像头（索引{self.cam_index}）")
            ret, _ = self.cap.read()
            if not ret:
                print("错误：无法读取摄像头画面")
        except Exception as e:
            print(f"错误：{e}")
            self.cap.release()

        