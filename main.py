from task import Task
from task_manager import TaskManager

manager = TaskManager()

task1 = Task(1, "Learn Python", "Practise OOP", "High")
task2 = Task(2, "Exercise", "Go for a run", "Medium")

manager.add_task(task1)
manager.add_task(task2)


task = manager.get_task(2)

#print(task)

print(manager.get_task(2))