from CADAR.camera import Camera
import numpy as np

cam = Camera(np.array([
    [1, 2, 1],
    [1, 2, 1],
    [1, 2, 1],
    ]))

cam.set_frame_rate(2)
print(cam.__doc__)
