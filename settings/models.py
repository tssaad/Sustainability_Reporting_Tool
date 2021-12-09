from django.db import models

continent_list = [
    ('EU','Europe'),
    ('AF','Africa'),
    ('NA','North America'),
    ('SA','South America'),
    ('AS','Asia'),
    ('AU','Australia'),
]



class Country(models.Model):
    name = models.CharField(max_length=225)
    continent = models.CharField(choices=continent_list, max_length=225)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name

class Province(models.Model):
    name = models.CharField(max_length=225)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=225)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name

