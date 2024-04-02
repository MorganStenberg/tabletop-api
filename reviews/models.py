from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    game = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(
        upload_to='images/', blank=True, null=True
    )
    rating = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
