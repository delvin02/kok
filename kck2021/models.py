from tkinter import CASCADE
from django.db import models
from django.utils.timezone import now
from datetime import datetime, date
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField 

from ckeditor_uploader.widgets import CKEditorUploadingWidget

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
    author = models.CharField(max_length=255, default="KCK")
    intro = models.TextField()
    body = RichTextUploadingField()
    date_added = models.DateTimeField(default=datetime.now)
    updated_date = models.DateTimeField(editable=False)
    categories = models.ManyToManyField(ArticleCategories,related_name="articleCategories")
   
    # ordered by 
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f"{self.id} | {self.title} | {self.date_added} "

    # def get_absolute_url(self):
    #     return reverse("kck:readblog", args=[self.slug,])

    def save(self, *args, **kwargs):
            if not self.id:  # Check if it's a new instance
                self.slug = slugify(self.title)  # Generate slug from title
                self.date_added = timezone.now()
            self.updated_date = timezone.now()
            super(Article, self).save(*args, **kwargs)

class Department(models.Model):
    agency = models.CharField(max_length=50)

    class Meta:
        ordering = ['agency']

    def __str__(self):
        return self.agency
    
class JobType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Career(models.Model):
    jobTypes = models.ManyToManyField(JobType, blank=True, related_name='careers')
    jobName = models.CharField(max_length=30)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="agencyName")
    jobLocation = models.CharField(max_length=30)
    link = models.URLField(default="#")
    timeAdded = models.DateField(default=datetime.now,blank=True)

    class Meta:
        ordering = ['jobName']
    
    def __str__(self):
        return f"{self.id} | {self.jobName} | {self.timeAdded}"
    
    def save(self, *args, **kwargs):
        if not self.id:  # Check if it's a new instance
            self.timeAdded = timezone.now()
        super(Career, self).save(*args, **kwargs)

class Job(models.Model):
    specialization = models.CharField(max_length=255);

    class Meta:
        ordering = ['specialization']

    def __str__(self):
        return self.specialization

class Project(models.Model):
    thumbnail = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=60, blank=False)
    slug = models.SlugField()
    body = RichTextUploadingField()
    mission = models.CharField(max_length=200, blank=False)
    location = models.CharField(max_length=100)
    jobType = models.ManyToManyField(Job, blank=False, related_name="job_spec")
    dateTime = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ['dateTime']

    def __str__(self):
        return self.title    

class ProjectImages(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="image")
    image = models.ImageField(upload_to='project/', blank=True)
    description = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} | {self.project.title}"

