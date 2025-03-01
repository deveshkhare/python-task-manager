# task_manager.py

class Task:
    """
    Represents a single task in the task manager.
    """

    def __init__(self, description, due_date=None):
        """
        Initializes a new Task object.

        Args:
            description (str): The task's description (e.g., "Buy groceries").
            due_date (str, optional): The task's due date (YYYY-MM-DD). Defaults to None.
        """
        # Assign the description to the task's description attribute
        self.description = description
        # Assign the due date to the task's due_date attribute
        self.due_date = due_date
        # Set the task's completion status to False by default
        self.completed = False

    def __str__(self):
        """
        Returns a string representation of the task.  This is what's printed
        when you use the `print()` function with a Task object.
        """
        # Create a string representing the task's completion status
        # "[x]" if the task is completed, "[ ]" otherwise
        status = "[x]" if self.completed else "[ ]"

        # Create a string representing the task's due date (if it has one)
        # If there's a due date, it's " (Due: YYYY-MM-DD)"; otherwise, it's an empty string
        due = f" (Due: {self.due_date})" if self.due_date else ""

        # Return a formatted string that includes the task's status, description, and due date
        return f"{status} {self.description}{due}"

    def mark_complete(self):
        """
        Marks the task as complete by setting the 'completed' attribute to True.
        """
        self.completed = True

class Task:
    """
    Represents a single task in the task manager.
    """

    def __init__(self, description, due_date=None):
        """
        Initializes a new Task object.

        Args:
            description (str): The task's description (e.g., "Buy groceries").
            due_date (str, optional): The task's due date (YYYY-MM-DD). Defaults to None.
        """
        # Assign the description to the task's description attribute
        self.description = description
        # Assign the due date to the task's due_date attribute
        self.due_date = due_date
        # Set the task's completion status to False by default
        self.completed = False

    def __str__(self):
        """
        Returns a string representation of the task.  This is what's printed
        when you use the `print()` function with a Task object.
        """
        # Create a string representing the task's completion status
        # "[x]" if the task is completed, "[ ]" otherwise
        status = "[x]" if self.completed else "[ ]"

        # Create a string representing the task's due date (if it has one)
        # If there's a due date, it's " (Due: YYYY-MM-DD)"; otherwise, it's an empty string
        due = f" (Due: {self.due_date})" if self.due_date else ""

        # Return a formatted string that includes the task's status, description, and due date
        return f"{status} {self.description}{due}"

    def mark_complete(self):
        """
        Marks the task as complete by setting the 'completed' attribute to True.
        """
        self.completed = True


class TaskManager:
    """
    Manages a collection of tasks.
    """

    def __init__(self):
        """
        Initializes a new TaskManager object with an empty list of tasks.
        """
        # Create an empty list to store the tasks
        self.tasks = []

    def add_task(self, description, due_date=None):
        """
        Adds a new task to the task list.

        Args:
            description (str): The task's description.
            due_date (str, optional): The task's due date (YYYY-MM-DD). Defaults to None.
        """
        # Create a new Task object
        task = Task(description, due_date)
        # Add the task to the list of tasks
        self.tasks.append(task)
        # Print a message to confirm that the task has been added
        print(f"Task added: {task}")

    def list_tasks(self):
        """
        Lists all tasks in the task list, showing their status (completed/pending).
        """
        # Check if the task list is empty
        if not self.tasks:
            # If the task list is empty, print a message
            print("No tasks yet!")
        else:
            # If the task list is not empty, iterate over the tasks
            for i, task in enumerate(self.tasks):
                # Print the task's index and string representation
                # Use i+1 for user-friendly indexing (starting from 1 instead of 0)
                print(f"{i+1}. {task}")

    def mark_complete(self, task_index):
        """
        Marks a task as complete, given its index in the task list.

        Args:
            task_index (int): The index of the task to mark as complete.
        """
        try:
            # Convert the task index to an integer and adjust for zero-based indexing
            task_index = int(task_index) - 1
            # Check if the task index is valid
            if 0 <= task_index < len(self.tasks):
                # Mark the task as complete
                self.tasks[task_index].completed = True
                # Print a message to confirm that the task has been marked as complete
                print(f"Task marked as complete: {self.tasks[task_index]}")
            else:
                # If the task index is invalid, print an error message
                print("Invalid task index.")
        except ValueError:
            # If the task index is not an integer, print an error message
            print("Invalid input. Please enter a number.")

    def delete_task(self, task_index):
        """
        Deletes a task from the task list, given its index.

        Args:
            task_index (int): The index of the task to delete.
        """
        try:
            # Convert the task index to an integer and adjust for zero-based indexing
            task_index = int(task_index) - 1
            # Check if the task index is valid
            if 0 <= task_index < len(self.tasks):
                # Delete the task from the list
                deleted_task = self.tasks.pop(task_index)
                # Print a message to confirm that the task has been deleted
                print(f"Task deleted: {deleted_task}")
            else:
                # If the task index is invalid, print an error message
                print("Invalid task index.")
        except ValueError:
            # If the task index is not an integer, print an error message
            print("Invalid input. Please enter a number.")