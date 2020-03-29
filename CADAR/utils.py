
def iou(box1, box2):
    S1 = (box1[2]-box1[0])*(box1[3]-box1[1])
    S2 = (box2[2]-box2[0])*(box2[3]-box2[1])
    intersection = (min(box1[2], box2[2])-max(box1[0], box2[0]))*(min(box1[3], box2[3])-max(box1[1], box2[1]))
    union = S1+S2-intersection
    IOU = intersection/union
    return IOU
