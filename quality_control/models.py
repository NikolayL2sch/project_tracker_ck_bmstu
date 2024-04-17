from django.db import models

from tasks.models import Project, Task


class BugReport(models.Model):
    STATUS_CHOICES = [('New', 'Новая'),
                      ('In progress', 'В работе'),
                      ('Completed', 'Завершена'), ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50,
                              choices=STATUS_CHOICES,
                              default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FeatureRequest(models.Model):
    STATUS_CHOICES = [('Pending', 'Рассмотрение'),
                      ('Approved', 'Принято'),
                      ('Rejected', 'Отклонено'), ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    priority = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
