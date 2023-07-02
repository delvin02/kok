from tkinter import CASCADE
from django.db import models
from django.utils.timezone import now
from tinymce import models as tinymce_models
from datetime import datetime, date
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from ckeditor.fields import RichTextField

from ckeditor_uploader.fields import RichTextUploadingField 

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from tinymce.models import HTMLField
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
        if not self.id:
            self.date_added = timezone.now()
        self.updated_date = timezone.now()
        return super(Article, self).save(*args, **kwargs)
    
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

class Text(models.Model):
    text = HTMLField()
