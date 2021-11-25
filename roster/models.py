from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=300, unique=True)
    title = models.CharField(max_length=200)
    bio = models.CharField(max_length=5000)
    image_url = models.CharField(max_length=500)
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Name: {self.name}, title: {self.title}, vote count: {self.vote_count}, object id = {self.id}"