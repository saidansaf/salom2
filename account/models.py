from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=False, null=False)
    age = models.PositiveSmallIntegerField(blank=True, default=18)
    bio = models.TextField(blank=True, null=True)  # ixtiyoriy bo'lishi uchun blank=True qo'shildi
    created_at = models.DateField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True)  # unique=True tavsiya etiladi

    REQUIRED_FIELDS = ['email', 'age', 'phone_number']

    def save(self, *args, **kwargs):
        if not self.slug:

            slug = slugify(f"{self.first_name}--{self.last_name}")
            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
