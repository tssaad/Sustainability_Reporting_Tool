from django.db import models
from settings.models import City, Country, Province

b_type= [
    ('Public', 'Public'),
    ('Private', 'Private'),
]
class Institute(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    type = models.ForeignKey("InstituteType", on_delete=models.CASCADE)
    specialty = models.ForeignKey("Specialty", on_delete=models.CASCADE)
    business_type = models.CharField(choices=b_type, max_length=225)

    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, blank=True, null=True)    
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    img = models.ImageField(upload_to="institute/", blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    class Meta:
        unique_together = ('name','country')

    def __str__(self):
        return self.name
    
class InstituteType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Specialty(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Specialties"

    def __str__(self):
        return self.name
