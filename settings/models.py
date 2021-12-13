from django.db import models

continent_list = [
    ('Europe','Europe'),
    ('Africa','Africa'),
    ('North America','North America'),
    ('South America','South America'),
    ('Asia','Asia'),
    ('Australia','Australia'),
]



class Country(models.Model):
    name = models.CharField(max_length=225, unique=True)
    continent = models.CharField(choices=continent_list, max_length=225)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name

class Province(models.Model):
    name = models.CharField(max_length=225, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=225, unique=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name

