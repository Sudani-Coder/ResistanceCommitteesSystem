from django.db import models
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from PIL import Image

GENDER = [
    ("male", "male"),
    ("female", "female"),
]

class Family(models.Model):
    IDTYPE = [
        ("PASSPT", "PassPort"),
        ("NNUMBER", "National Number"),
        ("NCARD", "National Card"),
    ]

    STATUS = [
        ("Single", "single"),
        ("Married", "married"),
        ("Divorced", "divorced"),
        ("Widowed", "widowed"),
    ]

    Id_Number = models.CharField(primary_key=True, max_length = 30)
    Id_Type = models.CharField(max_length = 7, choices = IDTYPE, default = "NNUMBER")
    Full_Name = models.CharField(max_length = 30)
    Age = models.PositiveIntegerField()
    Place_Of_Birth = models.CharField(max_length = 30)
    Gender = models.CharField(max_length = 6, choices = GENDER, default = "male")
    Social_Status = models.CharField(max_length = 8, choices = STATUS)
    Education_Level = models.CharField(max_length = 10)
    Job_Title = models.CharField(max_length = 20)
    Phone_Number = models.CharField(max_length = 10)
    Address = models.CharField(max_length = 200)
    House_Number = models.PositiveIntegerField()
    Family_Members_Number = models.PositiveIntegerField()
    Area = models.ForeignKey("Area", on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return self.Full_Name
    
    def get_absolute_url(self):
        return reverse('family-detail', kwargs = { 'pk': self.pk })

class FamilyMember(models.Model):
    Name = models.CharField(max_length = 150)
    Age = models.PositiveIntegerField()
    Gender = models.CharField(max_length = 6, choices = GENDER, default = "male")
    Relative_Relation = models.CharField(max_length = 100)
    Family = models.ForeignKey("Family", on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.Name
    
    def __repr__(self):
        return self.Name

class Area(models.Model):
    Area_Name = models.CharField(max_length = 20)

    def __str__(self):
        return self.Area_Name

    class Meta:
        ordering = ["Area_Name"]

    def get_absolute_url(self):
        return reverse('area-detail', kwargs = { 'pk': self.pk })

class Task(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField(blank = True, null = True)
    Price = models.PositiveIntegerField()
    Quantity = models.PositiveIntegerField()
    Complete = models.BooleanField(default = False)
    Created = models.DateTimeField(auto_now_add = True)
    Family = models.ForeignKey("Family", on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.Title
    
    def __repr__(self):
        return self.Title

    class Meta:
        ordering = ["-Created"]

class Project(models.Model):
    Title = models.CharField(max_length = 100)
    Description = models.TextField(blank = True, null = True)
    Project_Image = models.ImageField(blank = True, null = True)
    Complete = models.BooleanField(default = False)
    Created = models.DateTimeField(auto_now_add = True)
    Area = models.ForeignKey("Area", on_delete = models.SET_NULL, null = True)

    @property
    def image_url(self):
        if self.Project_Image and hasattr(self.Project_Image, 'url'):
            return self.Project_Image.url

    def __repr__(self):
        return self.Title

    def __str__(self):
        return self.Title

    class Meta:
        ordering = ["-Created"]

    def get_absolute_url(self):
        return reverse('project-detail', kwargs = { 'pk': self.pk })

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank = True, null = True, upload_to = 'profile_pics')
    Phone_Number = models.CharField(max_length = 10)
    Area = models.ForeignKey("Area", on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
