from django.db import models
from django.contrib.auth.models import User

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    sprite = models.CharField(max_length=2000)
    bio = models.TextField(max_length=1000)
    index = models.IntegerField(default = 0)
    can_evolve = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering =['index']
        
class Move(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    power = models.IntegerField(default= 0)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name="moves")
    
    def __str__(self):
        return self.name
    
class Group(models.Model):
    name = models.CharField(max_length=100)
    pokemons = models.ManyToManyField(Pokemon)
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    content: models.TextField(max_length=250)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name="comments")
    
    def __str__(self):
        return self.content

