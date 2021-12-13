from django.db import models

class IndexPage(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    img = models.ImageField(upload_to="pages/", blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title