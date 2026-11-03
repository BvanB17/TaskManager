from task import Task


class TaskManager():
    def __init__(self, ):
        self.tasks = []
        self.next_task_id = 1


    def add_task(self,existing_task, ):
        existing_task.task_id = self.next_task_id
        self.tasks.append(existing_task)
        self.next_task_id += 1
  
    def get_task(self, task_id):
        for task in self.tasks:
            if task_id == task.task_id:
                return task
            
        return None

    def remove_task(self, task_id):
        found_task = self.get_task(task_id)
        if found_task is None:
            return False
        else:
            self.tasks.remove(found_task)
        return True

    def complete_task(self, task_id,):
        found_task = self.get_task(task_id)
        if found_task is None:
            return False
        else:
            found_task.mark_complete()
        return True

    def get_all_tasks(self):
            return self.tasks

    def get_tasks_by_priority(self, priority,):
        found_tasks = []
        for task in self.tasks:
            if task.priority == priority.capitalize():
                found_tasks.append(task)
        return found_tasks

    def get_incomplete_tasks(self,):
        found_tasks = []
        for task in self.tasks:
            if not task.completed:
                found_tasks.append(task)
        return found_tasks    

    def update_task(self, task_id, option, new_value):
        found_task = self.get_task(task_id)
        if found_task is None:
            return False
        else:

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


