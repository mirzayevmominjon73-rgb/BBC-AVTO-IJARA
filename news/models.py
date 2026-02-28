from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news/')
    created_at = models.DateField(auto_now_add=True)
