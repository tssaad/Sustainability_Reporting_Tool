from django.db import models

from institute.models import Institute
from framework.models import Item

class AssessmentInfo(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # user
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    is_fininshed = models.BooleanField(default=False)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)

class WebsiteAssessmentDetail(models.Model):
    assessment_id = models.ForeignKey(AssessmentInfo, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    value = models.BooleanField(default=False)
