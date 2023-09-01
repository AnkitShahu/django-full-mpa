from django.db import models

# Create your models here.
class Home(models.Model):
    BannerTitle  = models.CharField(max_length=100)
    BannerSubtutle = models.CharField(max_length=100)
    btnTxt = models.CharField(max_length=100)
    btn2Txt = models.CharField(max_length=100)
    
    # bannertitle1 = models.CharField(max_length=100)
    # bannertitle1 = models.CharField(max_length=100)
    # bannertitle1 = models.CharField(max_length=100)
    # bannertitle1 = models.CharField(max_length=100)

    def __str__(self):
        return self.BannerTitle

# class Author(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()

#     def __str__(self):
#         return self.name

# class Entry(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     headline = models.CharField(max_length=255)
#     body_text = models.TextField()
#     pub_date = models.DateField()
#     mod_date = models.DateField()
#     authors = models.ManyToManyField(Author)
#     n_comments = models.IntegerField()
#     n_pingbacks = models.IntegerField()
#     rating = models.IntegerField()

class Doctor(models.Model):
    META_ROBOTS_CHOICES = (
        ('index', 'Index'),
        ('noindex', 'Noindex'),
    )

    META_FOLLOW_CHOICES = (
        ('follow', 'Follow'),
        ('nofollow', 'Nofollow'),
    )

    image = models.ImageField(upload_to='doctors/', null=True, blank=True)
    alt_tag = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    qualification = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    short_description = models.CharField(max_length=255, null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)
    expertise = models.CharField(max_length=100, null=True, blank=True)
    destination = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    profile_link = models.URLField(null=True, blank=True)
    slug = models.SlugField(max_length=250)
    meta_title = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    robots = models.CharField(max_length=10, choices=META_ROBOTS_CHOICES, null=True, blank=True)
    follow = models.CharField(max_length=10, choices=META_FOLLOW_CHOICES, null=True, blank=True)
    canonical_url = models.URLField(null=True, blank=True)
    schema = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    

class Contact(models.Model):
    OFFICE_LOCATIONS = (
        ('Main', '1040 SW 2nd Avenue, Ocala, FL'),
        ('West', '10230 SW 86th Circle, Ocala, FL'),
    )
    
    DOCTORS = (
        ('Ram Vasudevan, MD, FACC, FACP', 'Ram Vasudevan, MD, FACC, FACP'),
        ('Punwattie Ramnaraine, FNP-BC', 'Punwattie Ramnaraine, FNP-BC'),
        ('Alceha Mayne-Thomas, ARNP', 'Alceha Mayne-Thomas, ARNP'),
        ('Junaina Dominic, PA-C', 'Junaina Dominic, PA-C'),
        ('Emily Hawkins, APRN, NP-C', 'Emily Hawkins, APRN, NP-C'),
    )
    
    office_location = models.CharField(
        max_length=10, choices=OFFICE_LOCATIONS, default='Main', null=True, blank=True
    )
    doctor = models.CharField(
        max_length=100, choices=DOCTORS, null=True, blank=True
    )
    full_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.full_name
    
class OurMission(models.Model):
    missionTitle =  models.CharField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.missionTitle
    
class Services(models.Model):
    META_ROBOTS_CHOICES = (
        ('index', 'Index'),
        ('noindex', 'Noindex'),
    )

    META_FOLLOW_CHOICES = (
        ('follow', 'Follow'),
        ('nofollow', 'Nofollow'),
    )

    image = models.ImageField(upload_to='services/', null=True, blank=True)
    alt_tag = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=250)
    meta_title = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    robots = models.CharField(max_length=10, choices=META_ROBOTS_CHOICES, null=True, blank=True)
    follow = models.CharField(max_length=10, choices=META_FOLLOW_CHOICES, null=True, blank=True)
    canonical_url = models.URLField(null=True, blank=True)
    schema = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Faq(models.Model):
    category = models.ForeignKey(Services, on_delete=models.CASCADE)
    question = models.CharField(max_length=255, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.id) +" --- "+  str(self.category)
    
class SEO(models.Model):
    META_ROBOTS_CHOICES = (
        ('index', 'Index'),
        ('noindex', 'Noindex'),
    )

    META_FOLLOW_CHOICES = (
        ('follow', 'Follow'),
        ('nofollow', 'Nofollow'),
    )

    meta_title = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    robots = models.CharField(max_length=10, choices=META_ROBOTS_CHOICES, null=True, blank=True)
    follow = models.CharField(max_length=10, choices=META_FOLLOW_CHOICES, null=True, blank=True)
    canonical_url = models.URLField(null=True, blank=True)
    schema = models.TextField(null=True, blank=True)
    page = models.ForeignKey('Pages', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.page)
    
class Pages(models.Model):
    page = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.page