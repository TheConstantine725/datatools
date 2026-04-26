from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from multiprocessing import get_context
from orchestrator import TaskQueue
from time import sleep



def func_1():
    TaskQueue.put("Hail Mary")

def func_2():
    value = TaskQueue.get()
    print(value)
    sleep(1)


if __name__ == "__main__":
    with ProcessPoolExecutor(mp_context=get_context("fork")) as executor:
        executor.submit(func_1)
        executor.submit(func_2)
