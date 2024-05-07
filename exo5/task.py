from exception import InvalidTransition

class TaskStatus:
  TODO = 1
  DONE = 2
  CANCELED = 3

class Task:
  def __init__(self, name: str, priority: int = 10):
    self.name = name
    self.priority = priority
    self.status = TaskStatus.TODO

  def set_status(self, new_status: int):
    if self.status == TaskStatus.CANCELED and new_status == TaskStatus.DONE: raise InvalidTransition("Cannot mark a canceled task as done")
    self.status = new_status

class TaskList:
  def __init__(self, name: str):
    self.name = name
    self.tasks = []

  def create_task(self, name: str, priority: int = 10):
    task = Task(name, priority)
    self.tasks.append(task)

  def get_task_by_name(self, name: str):
    for task in self.tasks:
      if task.name == name: return task

  def get_all_task_names(self):
    return [task.name for task in self.tasks if task.status != TaskStatus.CANCELED]

  def get_tasks_by_priority(self, priority: int):
    return [task for task in self.tasks if task.priority == priority]

  def __str__(self):
    task_lines = sorted([f"[{task.priority}] {task.name}" for task in self.tasks if task.status != TaskStatus.CANCELED], key=lambda x: x.split(']')[0])
    title_line = f"== {self.name} =="
    total_line = f"Total: {len(task_lines)}"
    return "\n".join([title_line] + task_lines + [total_line])

