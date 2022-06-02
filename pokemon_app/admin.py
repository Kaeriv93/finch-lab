from django.contrib import admin
from .models import Pokemon, Move, Group, Comment

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Move)
admin.site.register(Group)
admin.site.register(Comment)

