from django.db import models
from django.contrib.auth.models import User
from saved.models import Save


class Game(models.Model):
    """
    Model for Games, related to user through owner and save model. 
    Which enables the user to create a game, to add to their wishlist
    and connect it to a saved review.
    """
    genre_choices = [
    ('strategy', 'Strategy'), 
    ('card_game', 'Card Game'), 
    ('casual', 'Casual'), 
    ('quiz', 'Quiz'), 
    ('deck_building', 'Deck Building'),
    ('cooperative', 'Cooperative'),
    ('party', 'Party'),
    ('puzzle', 'Puzzle'),
    ('adventure', 'Adventure'),
    ('role_playing', 'Role Playing'),
    ('simulation', 'Simulation'),
    ('trivia', 'Trivia'),
    ('other', 'Other')

    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    genre = models.CharField(
        max_length=40,
        choices=genre_choices,
        default='strategy')
    review_connect = models.ManyToManyField(Save, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

