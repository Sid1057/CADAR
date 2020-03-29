import cv2 as cv
import numpy as np


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
            # sda
            def append(self):
                pass
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


class CADAR:
    def __init__(self):
        self.last_img = None
        self.tracker = cv.TrackerKCF_create()
        self.objects = ObjectPool()
        self.velocity = 0.0
        pass

    def push(self, img):
        self.last_img = img
        if len(self.objects) != 0:
            success, boxes = self.tracker.update(self.last_img)
            (x, y, w, h) = [int(v) for v in boxes]

        for (box, label, score) in detect(img):
            self.objects.append(DetectedObject(box, label, score))

    def viz(self):
        viz = self.last_img.copy()
        for obj in self.objects.get_objects():
#             print(obj.box, obj.label, obj.score)
            print((obj.box[0], obj.box[1]), (obj.box[2], obj.box[3]), (0, 255, 0), 2)
            cv.rectangle(viz, (obj.box[0], obj.box[1]), (obj.box[2], obj.box[3]), (0, 255, 0), 2)
            cv.putText(viz, obj.label, (obj.box[0], obj.box[1]), 0, 1, (0, 255, 0), 2)
        return viz
#             cv.putText(viz, label+str(dist)+' m.', tuple(lu.astype(np.int32)), 0, 1, (0, 255, 0), 2)
