from django.db import models
from django.contrib.auth.models import User
from enum import Enum
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

    
class BlogPost(models.Model):
    class Tags(models.TextChoices):
        DATA_SCIENCE = 'DATA_SCIENCE', _('Data Science')
        DATA_ANALYSIS = 'DATA_ANALYSIS', _('Data Analysis')
        DATA_VISUALIZATION = 'DATA_VISUALIZATION', _('Data Visualization')
        MACHINE_LEARNING = 'MACHINE_LEARNING', _('Machine Learning')
        DEEP_LEARNING = 'DEEP_LEARNING', _('Deep Learning')
        ARTIFICIAL_INTELLIGENCE = 'ARTIFICIAL_INTELLIGENCE', _('Artificial Intelligence')
        NEURAL_NETWORKS = 'NEURAL_NETWORKS', _('Neural Networks')
        NATURAL_LANGUAGE_PROCESSING = 'NATURAL_LANGUAGE_PROCESSING', _('Natural Language Processing')
        COMPUTER_VISION = 'COMPUTER_VISION', _('Computer Vision')
        REINFORCEMENT_LEARNING = 'REINFORCEMENT_LEARNING', _('Reinforcement Learning')
        BIG_DATA = 'BIG_DATA', _('Big Data')
        CLOUD_COMPUTING = 'CLOUD_COMPUTING', _('Cloud Computing')
        INTERNET_OF_THINGS = 'INTERNET_OF_THINGS', _('Internet of Things')
        BLOCKCHAIN = 'BLOCKCHAIN', _('Blockchain')
        CYBER_SECURITY = 'CYBER_SECURITY', _('Cyber Security')
        WEB_DEVELOPMENT = 'WEB_DEVELOPMENT', _('Web Development')
        MOBILE_DEVELOPMENT = 'MOBILE_DEVELOPMENT', _('Mobile Development')
        GAME_DEVELOPMENT = 'GAME_DEVELOPMENT', _('Game Development')
        DEVOPS = 'DEVOPS', _('DevOps')
        DATABASES = 'DATABASES', _('Databases')
        PROGRAMMING_LANGUAGES = 'PROGRAMMING_LANGUAGES', _('Programming Languages')
        OTHER = 'OTHER', _('Other')

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = HTMLField()
    tag = models.CharField(max_length=200, choices=Tags.choices, default=Tags.OTHER)
    banner_image = models.ImageField(upload_to='blogs/banner_images/', blank=True)
    time_to_read = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Course(models.Model):
    class Types(models.TextChoices):
        PREMIUM = 'PREMIUM', _('Premium')
        GOLD = 'GOLD', _('Gold')
        WORKSHOPS = 'WORKSHOPS', _('Workshops')
        
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = HTMLField()
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    time_to_complete = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='courses/icons/', blank=True)
    banner_image = models.ImageField(upload_to='courses/banner_images/', blank=True)
    type = models.CharField(max_length=200, choices=Types.choices, default=Types.WORKSHOPS)
    link = models.URLField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CourseKeyPoint(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    key_point = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key_point

class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email