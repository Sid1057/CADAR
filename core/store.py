from .node import Node

from collections.abc import Iterable

class Storage:
    def __init__(self):
        self.callback = None
        pass

    # def

    def update(self):
        pass

class DataStore:
    def __init__(self, nodes):
        assert isinstance(nodes, Iterable)
        for node in nodes:
            assert isinstance(node, Node)
            
        self.nodes = nodes
        self.data = {}

    def push_data_sync(self, data_dict):
        # add atomic checking
        self.data = {}
        assert isinstance(data_dict, dict)

        self.data.update(data_dict)