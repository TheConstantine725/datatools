from .task import Task, Flow
from .result import Failure, Success, Result
from queue import Queue

TaskQueue = Queue(-1)

__all__ = ["Task", "Flow", "Failure", "Success", "Result", "TaskQueue"]
