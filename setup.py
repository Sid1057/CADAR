from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='CADAR',
    ext_modules=cythonize('CADAR/camera.pyx'))
