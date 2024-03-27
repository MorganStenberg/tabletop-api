from django.db import models

#Todo: add field for aggregating ratings from reviews
class Game(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title

