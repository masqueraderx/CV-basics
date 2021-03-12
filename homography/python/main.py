'''
chest robot project
Author: Xueren Ge
Time: Mar,12,2021
'''
import numpy as np
import json
import os
import cv2
import sys


def read_coordinate(filename):
    data = json.loads(filename)
    points = data['coordinates']
    return points

def H_transforamtion(filename, points):
    img = cv2.imread(filename)
    src_points = points
    dst_points = np.array([[70, 70], [950, 70], [950, 1060], [70, 1060]])
    H, _ = cv2.findHomography(src_points, dst_points)
    w = 1020
    h = 1130
    Perspective_img = cv2.warpPerspective(img, H, (w, h))
    return Perspective_img


if __name__ == '__main__':
    path = sys.argv[1]
    savepath = sys.argv[2]
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    points = np.array([[201, 318], [913, 313], [1006, 1137], [119, 1134]])
    for root, dirs, files in os.walk(path):
        for file in files:
            img_path = os.path.join(root, file)
            Perspective_img = H_transforamtion(img_path, points)
            savepath = os.path.join(savepath, os.path.basename(root)+'.jpg')
            cv2.imwrite(savepath, Perspective_img)



