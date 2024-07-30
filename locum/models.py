from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Section(models.Model):
    """
    Model for Category
    Stores a multiple blog post entries related to :model:`blog.Post`
    and :model:`post.Category`
    """
    class Meta:
        verbose_name_plural = 'Sections'
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Locum(models.Model):
    """
    Model for Posts
    Stores a single blog post entry related to :model:`auth.User`
    and :model:`blog.Post`.
    """
    title = models.CharField(max_length=250, unique=True)
    section = models.ForeignKey(Section, on_delete=models.PROTECT, default=4)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="locum_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User, related_name='locum_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

