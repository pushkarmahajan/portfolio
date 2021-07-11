from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=3000)
    image = models.ImageField(blank=True, upload_to='blog/images')

    def __str__(self):
        return self.title
