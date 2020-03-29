class Node:
	def __init__(self, inputs_map, outputs_map):
		assert isinstance(inputs_map, dict)
		assert isinstance(outputs_map, dict)