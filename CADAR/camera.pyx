import cython


@cython.cclass
class Camera:
    'Camera class interface'

    def __init__(self):
        pass

    def set_frame_rate(self, frame_rate: cython.int) -> bool:
        return True
