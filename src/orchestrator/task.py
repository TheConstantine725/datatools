from graphlib import TopologicalSorter
import traceback
from typing import (
    Callable,
    Sequence,
    Set,
    Union,
    Any,
    List,
    Tuple,
    Optional,
    Dict,
    override,
)
from hashlib import sha1, sha256
from time import sleep
from queue import Queue

type ArgsTuple[Any] = Union[List[Any], Tuple[Any]]


class Task:
    def __init__(
        self,
        task_name: str,
        task_description: Optional[str],
        action: Callable,
        args: ArgsTuple | dict[str, Any] | None,
        depends_on: "str" | tuple["str"] | set["str"] | list["str"] | None = None,
        retry_attempts: int = 3,
    ):
        self.task_name = task_name
        self.task_description = task_description
        self.action = action
        self.depends_on = depends_on
        self.args = args
        self.retry_attempts = retry_attempts
        self.execution_check = False

    @property
    def hash(self):
        return sha256(self.task_name.encode()).hexdigest()

    @override
    def __hash__(self):
        return hash(self.task_name)

    def _run_based_on_args(self):
        action_name = self.action.__name__
        if self.args is None:
            return self.action()
        elif isinstance(self.args, (tuple, list)):
            return self.action(*self.args)
        elif isinstance(self.args, dict):
            return self.action(**self.args)
        else:
            raise ValueError(
                f"Failed to run the action (task): {action_name} ({self.task_name})"
            )

    def execute(self):
        task_name = self.task_name
        for _ in range(1, self.retry_attempts + 1):
            try:
                print(f"Executing the {task_name=}({self.hash})")
                temp_output = self._run_based_on_args()
            except Exception as error:
                print(
                    "-" * 10,
                    text := f"ERROR START || Retry Attempt {_}",
                    "-" * (90 - len(text) - 2),
                )
                print(f"Error in the execution of the {task_name=}({self.hash})")
                print("=" * 100)
                print(error)
                print(
                    "-" * 10,
                    text := f"ERROR END || Retry Attempt {_}",
                    "-" * (90 - len(text) - 2),
                )
                print()
            else:
                print(f"Storing Result Output: {self.task_name=}")
                self.output = temp_output
                self.execution_check = True
                return self
        else:
            self.execution_check = True
            raise ValueError(f"Could not execute the task: {self.task_name}")


class Flow:
    def __init__(
        self,
        flow_name: str,
        flow_description: Optional[str],
    ):
        self.flow_name = flow_name
        self.flow_description = flow_description
        self.pending_tasks: Dict[str, Task] = dict()
        self.task_dependency_map: Dict[str, set[str]] = dict()
        self.task_results = dict()
        self.completed: dict[str, Task] = dict()
        self.failed: dict[str, Task] = dict()

    @property
    def hashname(self,):
        return sha1(self.flow_name.encode()).hexdigest()

    @override
    def __hash__(self):
        return hash(self.flow_name)

    def _settify_depending_tasks(self, task: Task) -> Set[str]:
        if task.depends_on is None:
            return set()
        elif isinstance(task.depends_on, str):
            return {task.depends_on}
        elif isinstance(task.depends_on, set):
            return task.depends_on
        elif isinstance(task.depends_on, (list, tuple)):
            return set(task.depends_on)

    def add_task(self, task: Task):
        try:
            self.pending_tasks[task.task_name] = task
            self.task_results[task.task_name] = None
            self.task_dependency_map[task.task_name] = self._settify_depending_tasks(
                task
            )
        except Exception as error:
            print(f"Error when adding {task.task_name}")
            print(error)
        else:
            return self

    def _prepare_execution_queue(self) -> Queue[str]:
        execution_queue = Queue(-1)
        sorter = TopologicalSorter()
        for node, deps in self.task_dependency_map.items():
            sorter.add(node, *deps)
        for taskname in sorter.static_order():
            execution_queue.put(taskname)
        return execution_queue

    def execute(self):
        exec_queue = self._prepare_execution_queue()
        while not exec_queue.empty():
            taskname = exec_queue.get()
            task = self.pending_tasks[taskname]
            try:
                result = task.execute()
            except Exception as error:
                print(error)
                self.failed[taskname] = task
            else:
                self.task_results[taskname] = result
                self.completed[taskname] = task
            finally:
                sleep(1)
