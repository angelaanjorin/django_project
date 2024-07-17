from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.


class About(models.Model):
    """
    Stores a single about me text
    """
    title = models.CharField(max_length=200)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title