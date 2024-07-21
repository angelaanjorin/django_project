from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
#from django.urls import reverse


User = get_user_model()

STATUS = ((0, "Draft"), (1, "Published"))


class Speciality(models.Model):
    """
    Model for Speciality
    Stores multiple job post entries related to :model:`jobs`
    and :model:`job.Speciality`
    """
    class Meta:
        verbose_name_plural = 'Speciality'
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    """
    Model to store user-submitted jobs
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="job_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)
    speciality = models.ForeignKey(Speciality, on_delete=models.PROTECT, default=4)
    created_on = models.DateTimeField(auto_now_add=True)
    location = models.TextField()
    dates = models.DurationField()
    link = models.URLField(blank=True)
    status = models.IntegerField(choices=STATUS, default=1)
    review = models.TextField(max_length=200)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title