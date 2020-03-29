import cv2 as cv
import numpy as np
from utils import iou

############ Raw structs
#
# RGB/Semantic
#
# RGBD/Semantic
#
# RGBDXYZ/Semantic
#
############ Object structs
#
### Object2D
#
# box2d
# label
# score
#
### Object3D
#
# object2d
# pointcloud?
# closest_point3d
#
### Object3D in time
#
# object3d
# lifetime
# object_vector
#
############ end

class DetectedObject:
    def __init__(self, box, label, score, lifetime=1):
        self.box = box
        self.label = label
        self.score = score
        self.lifetime = lifetime
        self.velocity = 0.0
        self.point3d = (0, 0, 0)
        
    def update(self, val=None):
        self.lifetime += 1

        if val is None:
            self.score **= 1.1
        else:
            self.score = max(self.score, val[2])


class ObjectPool:
    def __init__(self):
        self.objects = []

    def append(self, obj):  # associate
        best_idx = -1
        best_iou = 0
        best_tm = 64**2*255

        for idx, old_object in enumerate(self.objects):
            if best_iou < iou(old_object.box, obj.box):
                best_idx = idx
                best_iou = iou(old_object.box, obj.box)

        if best_iou < 0.55:
            self.objects.append(obj)
        else:
            self.objects[best_idx].box = [int((i+j)/2) for i, j in zip(self.objects[best_idx].box, obj.box)]
    
    def get_objects(self):
        for obj in self.objects:
            yield obj
            
    def __len__(self):
        return len(self.objects)