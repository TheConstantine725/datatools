from graphlib import TopologicalSorter
from threading import RLock
from typing_extensions import Any


class Registry(object):
    with RLock():
        _instance = None
        _registry = {}


    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Registry, cls).__new__(cls)
        return cls._instance

    @classmethod
    def add_asset(cls, asset: Any):
        if cls._registry["assets"] == None:
            pass
