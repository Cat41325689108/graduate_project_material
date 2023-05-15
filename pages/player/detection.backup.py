import cv2 as cv
import numpy as np


class Detector():
    def __init__(self, cap):
        self.fps = int(cap.get(cv.CAP_PROP_FPS))
        self.T_f = self.fps * 5
        self.initial_phase_i = 2
        self.initial_phase_done = False  # 初始化阶段是否完成
        self.frame_cur = None
        self.frame_pre = None
        self.F_avg = None
        self.F_sum = None




    def frame_in(self, frame):
        frame = cv.resize(frame, (360, 360))
        if self.frame_cur is None:
            self.frame_cur = frame
            return
        self.frame_pre = self.frame_cur
        self.frame_cur = frame
        frame_pre = self.frame_pre
        frame_cur = frame

        frame_pre = cv.cvtColor(frame_pre, cv.COLOR_BGR2GRAY)
        frame_pre = cv.Canny(frame_pre, 100, 200)
        frame_cur = cv.cvtColor(frame_cur, cv.COLOR_BGR2GRAY)
        frame_cur = cv.Canny(frame_cur, 100, 200)

        if self.F_sum is None:
            self.F_sum = np.zeros(frame_pre.shape)

        if self.initial_phase_done == False:
            self.F_sum += np.logical_and(frame_cur, frame_pre)
            self.initial_phase_i += 1
            if self.initial_phase_i >= self.T_f:
                self.initial_phase_done = True
                self.F_avg = self.F_sum / (self.T_f + 1)
            return 'normal'
        else:
            diff = np.logical_and(frame_cur, frame_pre)
            diff = np.sum(diff)
            F_avg = np.sum(self.F_avg)
            if diff > F_avg / 4:
                return 'normal'  # normal
            if diff <= F_avg / 4 and diff > F_avg / 10:
                return 'occlusion'  # occlusion
            return self.histogram_analyse(frame_cur, frame_pre)

    def histogram_analyse(self, frame, frame_pre):
        threshold_low, threshold_high = 72, 168
        alpha_motion = 1
        alpha_defocusing = 1.5

        hist = cv.calcHist(frame, [0], None, [256], [0, 255])
        hist_pre = cv.calcHist(frame_pre, [0], None, [256], [0, 255])
        sum = np.sum(hist[0:threshold_low + 1]) + np.sum(hist[threshold_high:256])
        sum_pre = np.sum(hist_pre[0:threshold_low + 1]) + np.sum(hist_pre[threshold_high:256])

        if sum * alpha_motion < sum_pre:
            return 'motion'  # motion occurs
        elif sum * alpha_defocusing < sum_pre:
            return 'defocusing'  # defocusing occurs
        return 'normal'  # normal
