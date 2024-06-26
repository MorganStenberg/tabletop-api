from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Credit to Code Institute walkthrough, link in readme.
class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)
    name = models.CharField(max_length=200, blank=True)
    favorite_game = models.CharField(max_length=250, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_yzvpjn'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
