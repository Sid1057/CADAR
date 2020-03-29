import cython
import numpy as np


@cython.cclass
class Camera:
    'Camera class interface'

    def __init__(self, initrics: np.array):
        'initrics: array 3x3 of initrics camera parameters such a focal length \
         and principial point'
        if not isinstance(initrics, np.ndarray):
            print('initrics type is ', type(initrics), 'expected npmy array')
            raise RuntimeError
        if not initrics.shape == (3, 3):
            print('initrics shape is ', initrics.shape)
            raise RuntimeError

        pass

    def set_frame_rate(self, frame_rate: cython.int) -> bool:
        return True

    def test(self, initrics: int):
        'initrics: array 3x3 of initrics camera parameters such a focal length \
         and principial point'
        print(np.__version__)
        pass


def test(initrics: int) -> int:
    'initrics: array 3x3 of initrics camera parameters such a focal length \
        and principial point'

    print(np.__version__)

    return initrics
