from task import Task


class TaskManager():
    def __init__(self, ):
        self.tasks = []
        self.next_task_id = 1


    def add_task(self,existing_task, ):
        existing_task.task_id = self.next_task_id
        self.tasks.append(existing_task)
        self.next_task_id += 1
        print(f"Ok, {existing_task} has been added to your task list!")
    

    def get_task(self, task_id):
        for task in self.tasks:
            if task_id == task.task_id:
                return task
            
        return None

    def remove_task(self, task_id):
        found_task = self.get_task(task_id)
        if found_task is not None:
            self.tasks.remove(found_task)
        else:
            print("Sorry, that task ID doesn't seem to match any current tasks.")



    def display_tasks(self):
        if not self.tasks:
            print("You are all caught up! There are no tasks!")
        else:
            for task in self.tasks:
                print(task)

    def update_task(self, task_id):
        found_task = self.get_task(task_id)
        if found_task is not None:
            method_choice = input("Which property do you want to edit?: ").capitalize()
        else:
            print("Sorry, that task ID doesn't seem to match any current tasks.")
            return

        if method_choice == "Title":
            new_title = input("Ok, you want to change the title to what?: ")
            found_task.update_title(new_title)
            return found_task
        elif method_choice == "Description":
            new_description = input("Ok, what is the new description of this task?: ")
            found_task.update_description(new_description)
            return found_task
        elif method_choice == "Priority":
            new_priority = input("Ok, what is the new level of Priority?: ")
            found_task.update_priority(new_priority)
            return found_task
        else:
            print("Sorry, this is not something that I can change for you.")