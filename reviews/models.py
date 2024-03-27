from django.db import models
from django.contrib.auth.models import User
from games.models import Game

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE,
        related_name='reviewed_games'
    )
    content = models.TextField()
    image = models.ImageField(
        upload_to='images/', blank=True, null=True
    )
    rating = models.IntegerField()


    class Meta: 
        ordering = ['-created_at']

    def __str__(self):
        return self.title