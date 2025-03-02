from django.db import models
from django.contrib.auth.models import User

class Golfer(models.Model):
    TIER_CHOICES = [
        (1, 'Tier 1'),
        (2, 'Tier 2'),
        (3, 'Tier 3'),
        (4, 'Tier 4'),
        (5, 'Tier 5'),
    ]
    name = models.CharField(max_length=100)
    tier = models.IntegerField(choices=TIER_CHOICES,default=3)

    def __str__(self):
        return f"{self.name} - Tier {self.tier}"
    
class FavoriteGolfer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #Link to user model
    golfer = models.ForeignKey(Golfer, on_delete=models.CASCADE) #LINK to golfer model

    def __str__(self):
        return f"{self.user.username}'s favorite golfer {self.golfer.name}"

    
