from task import Task


class TaskManager():
    def __init__(self, ):
        self.tasks = {}
        self.next_task_id = 1


    def add_task(self,existing_task, ):
        existing_task.task_id = self.next_task_id
        self.tasks[self.next_task_id] = existing_task
        self.next_task_id += 1
  
    def get_task(self, task_id):
        return self.tasks.get(task_id)

    def remove_task(self, task_id):
        found_task = self.get_task(task_id)
        if found_task is None:
            return False

        self.tasks.pop(task_id)
        return True

    def complete_task(self, task_id,):
        found_task = self.get_task(task_id)
        if found_task is None:
            return False

        found_task.mark_complete()
        return True

    def get_all_tasks(self):
        return list(self.tasks.values())

    def get_tasks_by_priority(self, priority,):
        found_tasks = []
        for task in self.tasks.values():
            if task.priority == priority.capitalize():
                found_tasks.append(task)
        return found_tasks

    def get_incomplete_tasks(self,):
        found_tasks = []
        for task in self.tasks.values():
            if not task.completed:
                found_tasks.append(task)
        return found_tasks    

    def update_task(self, task_id, option, new_value):
        found_task = self.get_task(task_id)
        if found_task is None:
            return False


        if option is None:
            return False
        elif option.capitalize() == "Title":
            found_task.update_title(new_value)
        elif option.capitalize() == "Description":
            found_task.update_description(new_value)
        elif option.capitalize() == "Priority":
            found_task.update_priority(new_value)
        else:
            return False
            
        return True


