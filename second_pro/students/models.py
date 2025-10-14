from django.db import models

class students(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

