

class Task:
    def __init__(self ,title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def update_priority(self, new_priority):
        if  self.priority== new_priority:
            print("This is already the priority of this task.")
        elif new_priority.capitalize() not in ["Low", "Medium", "High"]:
            print("Sorry, that is not one of the options, please pick: Low, Medium, or High.")
        else:
            self.priority = new_priority

    def update_title(self, new_title):
        if self.title == new_title:
            print("This is already the name of this Task.")
        else:
            self.title = new_title

    def update_description(self, new_description):
        if self.description == new_description:
            print("That is what you already have, please edit the description.")
        else:
            self.description = new_description




    def __str__(self):
        return f"Task: {self.title} | Priority: {self.priority} | Task ID: {self.task_id} \n Description: {self.description} | Completed?: {self.completed}"