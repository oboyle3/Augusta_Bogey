from django.db import models
from django.contrib.auth.models import User

class Golfer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class FavoriteGolfer(models.Models):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #Link to user model
    golfer = models.ForeignKey(Golfer, on_delete=models.CASCADE) #LINK to golfer model
    rank = models.IntegerField() #Rank 1 - 6 for top golfers

    class Meta:
        unique_together = ['user', 'rank'] #Ensure a user can only set 1 golfer per rank

    def __str__(self):
        return f"{self.user.username}'s favorite golfer"

    
