from django.db import models

# Create your models here.
# class Doctor(models.Model):
#     image = models.ImageField(upload_to='doctors/', null=True, blank=True)
#     name = models.CharField(max_length=100, null=True, blank=True)
#     qualification = models.CharField(max_length=100, null=True, blank=True)
#     location = models.CharField(max_length=100, null=True, blank=True)
#     short_description = models.CharField(max_length=255, null=True, blank=True)
#     long_description = models.TextField(null=True, blank=True)
#     expertise = models.CharField(max_length=100, null=True, blank=True)
#     destination = models.CharField(max_length=100, null=True, blank=True)
#     phone_number = models.CharField(max_length=20, null=True, blank=True)
#     email = models.EmailField(null=True, blank=True)
#     profile_link = models.URLField(null=True, blank=True)
    
    # def __str__(self):
    #     return self.name