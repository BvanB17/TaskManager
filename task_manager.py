from task import Task


class TaskManager():
    def __init__(self, ):
        self.tasks = {}
        self.next_task_id = 1


    def add_task(self,existing_task, ):
        if not isinstance(existing_task, Task):
            raise TypeError("You must pick a task.")
        
        existing_task.task_id = self.next_task_id
        self.tasks[self.next_task_id] = existing_task
        self.next_task_id += 1

        return existing_task.task_id
    

    def get_task(self, task_id):
        return self.tasks.get(task_id)

    def remove_task(self, task_id):
        found_task = self.get_task(task_id)
        if found_task is not None:
            del self.tasks[task_id]
            return True
        else:
            return False



    def display_tasks(self):
        if not self.tasks:
            return False
        else:
            for task in self.tasks.values():
                print(task)
            return True

    def update_task(self, task_id, property_name, new_value,):
        found_task = self.get_task(task_id)
        if found_task is None:
            return False
        if property_name == "Title":
            return found_task.update_title(new_value)
        elif property_name == "Description":
            return found_task.update_description(new_value)
        elif property_name == "Priority":
            return found_task.update_priority(new_value)            
        else:
            raise ValueError("Invalid Property Name.")