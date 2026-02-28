from django.db import models

class InterestSetting(models.Model):
    yearly_interest = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.yearly_interest}%"

