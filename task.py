

class Task:
    def __init__(self, title,description,priority):
        self.task_id = None
        if isinstance(priority, str) is False:
            raise TypeError("Please use a string with only letters.")
        
        if priority.capitalize() not in ["Low", "Medium", "High"]:
                raise ValueError("Priority must be either Low, Medium, or High.")
        self.priority = priority.capitalize()        
        if isinstance(title, str) is False:
            raise TypeError("Please use a string.")        
        if title.strip() == "":
            raise ValueError()
        self.title = title.strip()
        if not isinstance(description,str):
            raise ValueError()
        
        self.description = description
        self.completed = False


    def mark_complete(self):
        self.completed = True

    def update_priority(self, new_priority):
        if isinstance(new_priority, str):
            if  self.priority== new_priority:
                return False
            elif new_priority.capitalize() not in ["Low", "Medium", "High"]:
                return False
            else:
                self.priority = new_priority.capitalize()
                return True
        else:
            return False

    def update_title(self, new_title):
        if not isinstance(new_title,str):
            raise TypeError("Please use a string.")
        if new_title.strip() == "":
            raise ValueError("The list cannot be empty.")
        if self.title == new_title:
            return False
        else:
            self.title = new_title.strip()
            return True

    def update_description(self, new_description):
        if not isinstance(new_description,str):
            raise TypeError()
        if self.description == new_description:
            return False
        else:
            self.description = new_description
            return True




    def __str__(self):
        return f"Task: {self.title} | Priority: {self.priority} | Task ID: {self.task_id} \n Description: {self.description} | Completed?: {self.completed}"