import cv2 as cv
import numpy as np


class Detector():
    def __init__(self, cap):
        self.fps = int(cap.get(cv.CAP_PROP_FPS))
        self.T_f = self.fps * 5  # how many frames to be accumulated

        self.F_avg = 0
        self.F_sum = 0
        self.initial_stage = True
        self.initial_i = 2

        self.pre_frame = None
        self.cur_frame = None

        self.alpha = 1
        self.threshold_low = 72
        self.threshold_high = 168

        # 每次报警后暂停检测的时间
        self.pause_frame_i = 0
        self.pause_interval = 5 * self.fps  # frames
        self.alarm_pause = False

        self.detecte_interval = 3 * self.fps  # frames
        self.detecte_fram_i = 0
        self.alarm_results = []

    def canny(self, frame):
        f = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        f = cv.Canny(f, 100, 200)
        return f

    def gray(self, frame):
        return cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    def occlusion_detect(self):
        pre_frame = self.canny(self.pre_frame)
        cur_frame = self.canny(self.cur_frame)
        sim = np.logical_and(pre_frame, cur_frame)
        sim = np.sum(sim)
        # print(f'sim：{sim} ')
        if sim < self.F_avg / 3.5:
            # print(sim)
            return 'occlusion'

    def motion_detect(self):
        pre_frame = self.gray(self.pre_frame)
        cur_frame = self.gray(self.cur_frame)
        flow = cv.calcOpticalFlowFarneback(pre_frame, cur_frame, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        flow_avg = np.zeros(2)
        flow_avg[0] = np.mean(flow[..., 0])
        flow_avg[1] = np.mean(flow[..., 1])
        flow_len = np.linalg.norm(flow_avg)
        # print(flow_len)
        if flow_len > 7:
            return 'motion'
        if flow_len > 2:
            return 'shake'

    def frame_in(self, frame):
        frame = cv.resize(frame, (360, 360))
        f = frame
        if self.cur_frame is None:
            self.cur_frame = f
            return None
        else:
            self.pre_frame = self.cur_frame
            self.cur_frame = f

        if self.initial_stage == True:
            self.__initialize()
            return None
        else:
            if self.alarm_pause == True:  # 已经报警
                self.pause_frame_i += 1
                if self.pause_frame_i > self.pause_interval:
                    self.pause_frame_i = 0
                    self.alarm_pause = False
                return None

            self.detecte_fram_i += 1
            occlusion = self.occlusion_detect()
            motion = self.motion_detect()
            if occlusion != None:
                self.alarm_results.append(occlusion)
            if motion != None:
                self.alarm_results.append(motion)

            if self.detecte_fram_i > self.detecte_interval:
                self.detecte_fram_i = 0
                if len(self.alarm_results) != 0:
                    self.alarm_pause = True
                    if 'motion' in self.alarm_results:
                        return 'motion'
                    elif self.alarm_results.count('shake') > 4:
                        return 'shake'
                    else:
                        return 'occlusion'

    def __initialize(self):
        pre_frame = self.canny(self.pre_frame)
        cur_frame = self.canny(self.cur_frame)
        diff = np.logical_and(pre_frame, cur_frame)
        if self.F_sum is None:
            self.F_sum = np.zeros(pre_frame.shape)
        self.F_sum += diff
        self.initial_i += self.detecte_interval
        if self.initial_i >= self.T_f:
            self.F_avg = np.sum(self.F_sum / (self.T_f + 1))
            self.initial_stage = False
