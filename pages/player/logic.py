import os

files = []


def get_local_videos(self):
    global files
    filePath = './occlusion_detection/datas'
    files = os.listdir(filePath)

