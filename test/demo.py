#!/env/bin/python3

import cv2 as cv
import numpy as np

import glob
import os

import sys
try:
	sys.path.append('..')
	from core.node import Node
	from core.stereo import SGBM
	from core.store import DataStore
except ImportError as error:
	print(error)
	raise

data_folder = '../data/carla_sequence_00/'
left_dir = data_folder+'/left/'
right_dir = data_folder+'/right/'
depth_dir = data_folder+'/depth/'
semantic_dir = data_folder+'/semantic/'

names = sorted([os.path.basename(i) for i in glob.glob(left_dir+'/*')])

stereo = SGBM({}, {})
store = DataStore([stereo])

for name in names:
	left = cv.imread(left_dir+name)
	right = cv.imread(right_dir+name)
	semantic = cv.imread(semantic_dir+name)
	depth = cv.imread(depth_dir+name)

	store.push_data_sync({
		'left': left,
		'right': right,
		'calibration_paremeters': None
		'semantic': semantic[..., 2],
		'obstacles_mask': cv.inRange(semantic[..., 2], 6, 8),  # рассказать о таком подходе к разработке с помощью симулятора
		'depth': depth,
		})

	cv.imshow('left', left)
	cv.imshow('depth', depth)
	# cv.imshow('semantic', store.data['obstacles_mask'])

	key = cv.waitKey(200)
	if key == ord('q'):
		break