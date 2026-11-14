class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.is_done = False

    def complete(self):
        self.is_done = True


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        self.tasks.append(Task(description, deadline))

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete()

    def show_current_tasks(self):
        for i, task in enumerate(self.tasks):
            if not task.is_done:
                print(f"{i}. {task.description} (до {task.deadline})")


# Пример использования
manager = TaskManager()
manager.add_task("Изучить классы в Python", "15.11.2026")
manager.add_task("Загрузить код на GitHub", "16.11.2026")
manager.mark_completed(0)
manager.show_current_tasks()
