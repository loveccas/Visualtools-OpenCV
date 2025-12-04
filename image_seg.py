import cv2
import numpy as np
from video import Video


class ImageSegmentation(Video):
    def __init__(self,LAB_thresholds={'L':(0,255),'A':(0,255),'B':(0,255)}):
        super().__init__()
        self.LAB_thresholds = LAB_thresholds
        self.L_min, self.L_max = self.LAB_thresholds['L']
        self.A_min, self.A_max = self.LAB_thresholds['A']
        self.B_min, self.B_max = self.LAB_thresholds['B']
    
    def get_LAB_threshold(self):
        def process_frame(frame):
            lab_img = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
            L, A, B = cv2.split(lab_img)
            mask_L = cv2.inRange(L, self.L_min, self.L_max)
            mask_A = cv2.inRange(A, self.A_min, self.A_max)
            mask_B = cv2.inRange(B, self.B_min, self.B_max)
            mask = cv2.bitwise_and(mask_L, cv2.bitwise_and(mask_A, mask_B))
            return mask
        def update_L_min(val):
            self.L_min = val
        def update_L_max(val):
            global L_max
            self.L_max = val
        def update_A_min(val):
            global A_min
            self.A_min = val
        def update_A_max(val):
            global A_max
            self.A_max = val
        def update_B_min(val):
            global B_min
            self.B_min = val
        def update_B_max(val):
            global B_max
            self.B_max = val
        cv2.namedWindow("LAB", cv2.WINDOW_NORMAL)
        cv2.createTrackbar("L_min", "LAB", self.L_min, 255, update_L_min)
        cv2.createTrackbar("L_max", "LAB", self.L_max, 255, update_L_max)
        cv2.createTrackbar("A_min", "LAB", self.A_min, 255, update_A_min)
        cv2.createTrackbar("A_max", "LAB", self.A_max, 255, update_A_max)
        cv2.createTrackbar("B_min", "LAB", self.B_min, 255, update_B_min)
        cv2.createTrackbar("B_max", "LAB", self.B_max, 255, update_B_max)

        try:
            while True:
                ret, frame = self.cap.read()
                if not ret :
                    continue
                mask = process_frame(frame)
                cv2.imshow("mask", mask)
                if cv2.waitKey(1)== ord('q') or cv2.waitKey(1)== 27:
                    break
        finally:
            self.cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    image_seg = ImageSegmentation(LAB_thresholds={'L':(0,255),'A':(0,255),'B':(0,255)})
    image_seg.get_LAB_threshold()
