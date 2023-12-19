from django.db import models
from category.models import Category

class task(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    is_completed = models.BooleanField(default=False)  # Default value set to False
    task_assign_date = models.DateTimeField(auto_now_add=True)  # Assigns the current date and time when the task is created

    def __str__(self):
        return self.title
