from django.db import models
from django.db.models.fields import BooleanField

class Item(models.Model):
    item = models.TextField() 
    description = models.TextField() 
    is_active = models.BooleanField(default=True)
    dimension = models.ForeignKey("Dimension", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.item
    

class Dimension(models.Model):
    name = models.TextField()
    description = models.TextField()
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, limit_choices_to={'parent__isnull': True})
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    