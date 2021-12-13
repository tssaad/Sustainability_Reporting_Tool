from django.db import models

from institute.models import Institute
from framework.models import Item

from authentication.models import User

class WebAssessmentInfo(models.Model):
    name = models.CharField(max_length=255, verbose_name="Assessment Name")
    description = models.TextField(verbose_name="Assessment Description")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now=True)
    finish_at = models.TimeField(blank=True, null=True)
    is_fininshed = models.BooleanField(default=False)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, verbose_name="Website of Institute to be assessed")

    class Meta:
        verbose_name_plural = "Web Assessment Info"

class WebsiteAssessmentDetail(models.Model):
    asessment = models.ForeignKey(WebAssessmentInfo, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now=True)
    updated_at = models.TimeField(auto_now_add=True)
    value = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Website Assessment Details"
