from tkinter import CASCADE
from django.db import models
from django.utils.timezone import now
from datetime import datetime, date
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField 
from django.urls import reverse
from ckeditor_uploader.widgets import CKEditorUploadingWidget
import uuid
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

# Create your models here.

class ArticleCategories(models.Model):
    category = models.CharField(max_length=60)
    
    class Meta:
        ordering = ['category']
        verbose_name_plural = "Articles - Categories"


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
        verbose_name_plural = "Articles"


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

    def get_absolute_url(self):
        return reverse('kck:readblog', kwargs={'slug_name': self.slug})
class Department(models.Model):
    agency = models.CharField(max_length=50)

    class Meta:
        ordering = ['agency']
        verbose_name_plural = "Careers - Departments"


    def __str__(self):
        return self.agency
    
class JobType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Careers - Job Type"
    
class Career(models.Model):
    jobTypes = models.ManyToManyField(JobType, blank=True, related_name='careers')
    jobName = models.CharField(max_length=30)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="agencyName")
    jobLocation = models.CharField(max_length=30)
    link = models.URLField(default="#")
    timeAdded = models.DateField(default=datetime.now,blank=True)

    class Meta:
        ordering = ['jobName']
        verbose_name_plural = "Careers"

    
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
        verbose_name_plural = "Projects - Jobs"

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
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title    

class ProjectImages(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="image")
    image = models.ImageField(upload_to='project/', blank=True)
    description = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} | {self.project.title}"
    
    class Meta:
        verbose_name_plural = "Projects - Images"

class LegalCategory(models.Model):
    category = models.CharField(max_length=64)
    class Meta:
        ordering = ['category']
        verbose_name_plural = "Legal - Categories"


    def __str__(self):
        return self.category
    
class Company(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Legal - Companies"


    def __str__(self):
        return self.name    
class Legal(models.Model):
    title = models.CharField(max_length=60, blank=False)
    slug = models.SlugField(unique=True)
    body = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(
        LegalCategory,
        on_delete=models.CASCADE,
        related_name='legal_category'
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='companies',
        blank = True,
        null = True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Legal - Terms"

    def save(self, *args, **kwargs):
        # Check if the object is already in the database
        if self.pk:
            old_legal = Legal.objects.get(pk=self.pk)
            if old_legal.title != self.title:
                self.slug = slugify(self.title)
        else:
            # This is a new object, so create a slug
            self.slug = slugify(self.title)

        # Always update the 'updated' timestamp
        self.updated = timezone.now()

        super(Legal, self).save(*args, **kwargs)

    def get_absolute_url(self):
        if self.company:
            return reverse('kck:legal_with_company', kwargs={'company_name': self.company.name.lower(), 'slug': self.slug})
        else:
            return reverse('kck:legal_without_company', kwargs={'slug': self.slug})


class IdentityStatus(models.Model):
    status = models.CharField(max_length=255)

    class Meta:
        ordering = ['status']
        verbose_name_plural = "Identity - Status"


    def __str__(self):
        return self.status  

'''
    IMAGE PATH FOR IDENTITY
'''


def unique_upload_path(instance, filename, folder_name):
    phone = instance.phone
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    ext = filename.split('.')[-1]
    new_filename = f"{now}.{ext}"
    return f'identity/{phone}/{folder_name}/{new_filename}'

def front_image_upload_path(instance, filename):
    # Call the generic function with 'front' as the folder name
    return unique_upload_path(instance, filename, 'front')

def back_image_upload_path(instance, filename):
    # Call the generic function with 'back' as the folder name
    return unique_upload_path(instance, filename, 'back')

def selfie_image_upload_path(instance, filename):
    # Call the generic function with 'selfie' as the folder name
    return unique_upload_path(instance, filename, 'selfie')


class IdentityRegister(models.Model):
    reference_code = models.CharField(max_length=20, unique=True, editable=False)
    phone = models.CharField(max_length=20, blank=False)
    front = models.ImageField(upload_to=front_image_upload_path, blank=False)
    back = models.ImageField(upload_to=back_image_upload_path, blank=False)
    selfie = models.ImageField(upload_to=selfie_image_upload_path, blank=False)
    
    name = models.TextField(blank=True)
    verified = models.BooleanField(default=False)
    statuses = models.ManyToManyField(IdentityStatus)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['reference_code']
        verbose_name_plural = "Identity"

    def __str__(self):
        return self.reference_code
    
    def clean(self):
        # Custom validation logic
        if self.verified and not self.name:
            raise ValidationError({'name': gettext_lazy("Nama wajib di-isi untuk memenuhi proses verifikasi.")})
        

    def save(self, *args, **kwargs):

        if not self.pk:  
            last_instance = IdentityRegister.objects.order_by('-id').first()
            last_id = last_instance.id if last_instance else 0
            primary_id = last_id + 1 
            last_three_digits = self.phone[-3:] 
            self.reference_code = f'SEMIX{str(primary_id).zfill(4)}-{last_three_digits}'

        
        
        self.clean()

        super(IdentityRegister, self).save(*args, **kwargs) 


        if not self.statuses.exists():
            default_status, _ = IdentityStatus.objects.get_or_create(status="Belum disemak")
            self.statuses.add(default_status)

    def get_absolute_url(self):
        return reverse('kck:identity_register_status', kwargs={'reference_code': self.reference_code})

class IdentityRegisterChangeLog(models.Model):
    identity_register = models.ForeignKey(IdentityRegister, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
    
    
class ReuploadToken(models.Model):
    identity_register = models.ForeignKey(IdentityRegister, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, unique=True)
    expires_at = models.DateTimeField()

    @property
    def is_valid(self):
        return timezone.now() < self.expires_at