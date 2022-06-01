from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    sprite = models.CharField(max_length=2000)
    bio = models.TextField(max_length=1000)
    index = models.IntegerField(default = 0)
    can_evolve = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

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