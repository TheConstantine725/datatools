def main():
    from graphlib import TopologicalSorter
    temp = {"task3": {"task1", "task2"}, "task4": {"task3", "task1"}, "task5":{}}
    sorter = TopologicalSorter()
    for task, deps in temp.items():
        if deps is None:
            sorter.add(task, None)
        else:
            sorter.add(task, *deps)
    try:
        result = sorter.static_order()
    except Exception as error:
        print(error)
    else:
        return result

if __name__ == "__main__":
    for _ in main():
        print(_)
