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