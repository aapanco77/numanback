from django.conf import settings
from django.db import models
from django.utils import timezone

class Team(models.Model):
    coworker = models.CharField(max_length=30)
    status = models.CharField(max_length=20)
    assign_project = models.CharField(max_length=20)

    def __str__(self):
        return self.coworker

class Project(models.Model):
    """Proyectos de marca"""
    company = models.CharField(max_length=20)
    progress = models.SmallIntegerField(null=True, blank=True)
    death_line = models.DateTimeField(default=timezone.now)
    url_drive = models.URLField(null=True)
    dummies = models.CharField(max_length=20)

    class Meta:
        ordering = ['company', ]

    def __str__(self):
        return self.company