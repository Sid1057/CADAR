import torchvision
from torchvision import transforms as T
import torch
import cv2 as cv

COCO_INSTANCE_CATEGORY_NAMES = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',
    'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',
    'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
    'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]


class Detector:
    def __init__(self, min_size=320):
        self.faster_rcnn = torchvision.models.detection.fasterrcnn_resnet50_fpn(
            pretrained=True, min_size=min_size).cuda().eval()
        self.transform = T.Compose([
                T.ToPILImage(),
                T.ToTensor()
            ])

    def detect(self, img, threshold=0.5):
        with torch.no_grad():
            tensor = self.transform(
                cv.cvtColor(img, cv.COLOR_BGR2RGB)).cuda()
            detected = self.faster_rcnn([tensor])[0]
            tensor.cpu()

            boxes = detected['boxes'].cpu().numpy()
            labels = detected['labels'].cpu().numpy()
            scores = detected['scores'].cpu().numpy()

            return [
                ([*box], COCO_INSTANCE_CATEGORY_NAMES[label], score)
                    for (box, label, score) in zip(boxes, labels, scores) if score>threshold]