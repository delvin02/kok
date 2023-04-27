from tkinter import CASCADE
from django.db import models
from django.utils.timezone import now
from tinymce import models as tinymce_models
from tinymce.models import HTMLField
from datetime import datetime, date
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
# Create your models here.

class ArticleCategories(models.Model):
    category = models.CharField(max_length=60)
    
    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.category

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    thumbnail = models.ImageField(upload_to='static/img/blog/')
    month = models.CharField(max_length=10)
    day = models.PositiveIntegerField()
    author = models.CharField(max_length=255, default="False")
    intro = models.TextField()
    body = tinymce_models.HTMLField()
    date_added = models.DateTimeField(default=datetime.now)
    categories = models.ManyToManyField(ArticleCategories,related_name="articleCategories")
   
    # ordered by 
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f"{self.id} | {self.title} | {self.date_added} "

    def get_absolute_url(self):
        return reverse("kck:readblog", args=[self.slug,])
    
class Department(models.Model):
    agency = models.CharField(max_length=50)

    class Meta:
        ordering = ['agency']

    def __str__(self):
        return self.agency

class Career(models.Model):
    jobName = models.CharField(max_length=30)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="agencyName")
    imageLogo = models.ImageField(upload_to='static/img/job/')
    jobLocation = models.CharField(max_length=30)
    estimatedSalary = models.PositiveIntegerField(
            default=1000,
            validators=[
            MaxValueValidator(10000),
            MinValueValidator(1)
        ]
    )
    timeAdded = models.DateField(default=datetime.now,blank=True)

    class Meta:
        ordering = ['jobName']
    
    def __str__(self):
        return f"{self.id} | {self.jobName} | {self.timeAdded}"

class Job(models.Model):
    specialization = models.CharField(max_length=255);

    class Meta:
        ordering = ['specialization']

    def __str__(self):
        return self.specialization

class ProjectImages(models.Model):
    image = models.ImageField(upload_to='project/', null=True, blank=False)
    
    def __str__(self):
        return self.image

class Project(models.Model):
    thumbnail = models.ImageField(upload_to='media/')
    openingImage = models.ImageField(upload_to='media/')
    projectIntro = tinymce_models.HTMLField()
    title = models.CharField(max_length=60, blank=False)
    slug = models.SlugField()
    mission = models.CharField(max_length=200, blank=False)
    location = models.CharField(max_length=100)
    value = models.DecimalField(max_digits =4,decimal_places=2)
    jobType = models.ManyToManyField(Job, blank=False, related_name="job_spec")
    photos = models.ForeignKey(ProjectImages, on_delete=models.CASCADE, null=True, blank=True, related_name="images")
    dateTime = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ['dateTime']

    def __str__(self):
        return self.title
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    images = models.ImageField(upload_to='media/', blank=True)

