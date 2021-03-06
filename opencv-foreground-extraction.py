# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 22:23:44 2018

@author: guest11
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('my.jpg')
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)
rect = (200, 0, 830, 390)

cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()
# =============================================================================
# cv2.rectangle(img, (550,0), (830,390), (0,255,0),3)
# cv2.imshow('my',img)
# =============================================================================

cv2.waitKey(0)
cv2.destroyAllWindows()