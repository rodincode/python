# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 17:32:29 2020

@author: LENOVO
"""

import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
im = cv2.imread('apple-256261_640.jpg')
bbox, label, conf = cv.detect_common_objects(im)
output_image = draw_bbox(im, bbox, label, conf)
plt.imshow(output_image)
plt.show()