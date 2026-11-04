

class Task:
    def __init__(self, title,description,priority):
        self.task_id = None
        if not isinstance(priority, str):
            raise TypeError("Please use a string with only letters.")        
        if priority.capitalize() not in ["Low", "Medium", "High"]:
                raise ValueError("Priority must be either Low, Medium, or High.")
        self.priority = priority.capitalize()        
        if not isinstance(title, str):
            raise TypeError("Please use a string.")        
        if title.strip() == "":
            raise ValueError("The Title cannot be empty.")
        self.title = title.strip()
        if not isinstance(description,str):
            raise TypeError("Please use a string.")
        
        self.description = description
        self.completed = False


    def mark_complete(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

    def update_priority(self, new_priority):
        if not isinstance(new_priority, str):
            raise TypeError("Priority must be a String.")

        new_priority = new_priority.capitalize()

        if new_priority not in ["Low", "Medium", "High", ]:
            raise ValueError("Priority must be Low, Medium, or High.")
        if self.priority == new_priority:
            return False

        self.priority = new_priority
        return True
        

    def update_title(self, new_title):
        if not isinstance(new_title,str):
            raise TypeError("Please use a string.")
        new_title = new_title.strip()
        if new_title == "":
            raise ValueError("The list cannot be empty.")
        if self.title == new_title:
            return False
        else:
            self.title = new_title
            return True

    def update_description(self, new_description):
        if not isinstance(new_description,str):
            raise TypeError("Please use a string.")
        if self.description == new_description:
            return False
        else:
            self.description = new_description
            return True




    def __str__(self):
        return f"Task: {self.title} | Priority: {self.priority} | Task ID: {self.task_id} \n Description: {self.description} | Completed?: {self.completed}"