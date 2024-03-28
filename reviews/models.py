from django.db import models
from django.contrib.auth.models import User

#Todo: add field for aggregating ratings from reviews
class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    game = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(
        upload_to='images/', blank=True, null=True
    )
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)



    class Meta: 
        ordering = ['-created_at']

    def __str__(self):
        return self.title