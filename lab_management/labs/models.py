from django.db import models

class Lab(models.Model):
    name = models.CharField(max_length=100, unique=True)
    instructor = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
