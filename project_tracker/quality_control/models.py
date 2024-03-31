from django.db import models
from tasks.models import Project
from tasks.models import Task


# Create your models here.
class BugReport(models.Model):
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]
    PRIORITY_CHOICES = [
        ('High', 'Высокий'),
        ('Middle', 'Средний'),
        ('Low', 'Низкий'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FeatureReport(models.Model):
    STATUS_CHOICES = [
        ('On_consideration', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Denied', 'Отклонено'),
    ]
    PRIORITY_CHOICES = [
        ('High', 'Высокий'),
        ('Middle', 'Средний'),
        ('Low', 'Низкий'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='On_consideration'
    )
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
