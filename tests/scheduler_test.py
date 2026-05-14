from datetime import datetime
from threading import Lock
from typing import Self
from orchestrator.task import Flow


class Registry:
    with Lock():
        _instance = None

    flows = dict()
    event_map: dict[datetime, str] = dict()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super.__new__(cls)
        return cls._instance

    @classmethod
    def add_flow(cls, flow: Flow):
        cls.flows[flow.hashname] = flow
        return cls


class Scheduler:
    pass
