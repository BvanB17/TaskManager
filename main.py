from task import Task
from task_manager import TaskManager

manager = TaskManager()
task1 = Task("Test Task","This is just a test.", "Low",)
manager.add_task(task1)



def main():

    running = True
    print("Welcome to the Manager!")

    while running:
        print("What would you like to do?")
        print("1. List tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Remove task")
        print("5. Exit")    

        choice = input("Select an Option: ")

        if choice == "1":
            if manager.tasks:
                for task in manager.tasks.values():
                    print(task)
            else:
                    print("Hooray, you have no tasks!")


        elif choice == "2":
                print("Ok, let's add a new Task.")
                new_task_title = input("What will be the title for this Task?")
                new_task_description = input("Provide a brief description of the Task.")
                new_task_priority = input("Should the Priority be Low, Medium, or High?")

                try:
                    new_task = Task(new_task_title,new_task_description,new_task_priority)
                    manager.add_task(new_task)
                except (ValueError, ) as error:
                    print(error)
                except (TypeError, ) as error:
                     print(error)
                else:
                    print(f"Ok, we have added {new_task_title} to the list as Task ID:{new_task.task_id}")

        elif choice == "3":

            property_to_update = input("What is the Property you want to update?: ")
            updated_value = input("What should be the new value for this Property?: ")

            try:
                task_to_update_id = int(input("What is the Task ID of the task you want to update?: "))
                update_result = manager.update_task(task_to_update_id, property_to_update, updated_value, )
            except (ValueError) as error:
                 print(error)
            except (TypeError, ) as error:
                 print(error)
            else:
                if update_result:
                    print(f"Ok, The new value of {property_to_update} is  {updated_value}!")

        elif choice == "4":

            task_to_remove_id = int(input("What is the Task ID of the task you want to update?: "))
            print(manager.tasks[task_to_remove_id])
            make_sure = input("Are you sure you want to delete this task?(y/n): ").strip()


            if make_sure == "y":

                try:
                    task_to_remove = manager.remove_task(task_to_remove_id)
                    if task_to_remove:
                        print(f"Okay, {task_to_remove_id}| is gone!")
                except (ValueError) as error:
                    print(error)

            print("Okay, returning to menu.")    


        elif choice == "5":
            print("Shutting Down...")
            running = False


if __name__ == "__main__":
    main()