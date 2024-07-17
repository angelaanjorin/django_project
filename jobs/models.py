from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver


STATUS = ((0, "Draft"), (1, "Published"))
User = get_user_model()


class Profile(models.Model):
    """
    Model for user profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_picture = CloudinaryField('image', default='placeholder')
    firstname = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    speciality = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True)
    cv = models.FileField(
        upload_to="profiles/",
        blank=False,
    )

    def __str__(self):
        return f'{self.user.username} Profile'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create or update the user profile"""
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()


class Employer(models.Model):
    """
    Model for employer profile
    """
    user = models.OneToOneField(User, related_name="employer", on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=30, blank=True, null=True)
    institution = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Jobs(models.Model):
    """
    Model to store employer-submitted jobs
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="job_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)
    speciality = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    location = models.TextField()
    dates = models.DurationField()
    job_info = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Jobs, self).save(*args, **kwargs)