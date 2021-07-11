from django.db import models

# Create your models here.


class Project(models.Model):  # inheriting model class
    # we can use django model fields to see what data type is suitable for us
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    # for using image field we need to install pillow
    image = models.ImageField(upload_to="portfolio/images")
    # blank is supported by every field, it is used to specify
    url = models.URLField(blank=True)
    # that if a field can be (empty or not) or (mandatory or not)

    def __str__(self):
        return self.title
