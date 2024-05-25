from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone=models.CharField(max_length=100)
    city= models.CharField(max_length=100,null=True)
    state= models.CharField(max_length=100,null=True)
    pincode= models.IntegerField(null=True)
    image= models.ImageField(upload_to='images',null=True)
    user_file = models.FileField(upload_to='cv_files/',null=True)

class JobPost(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE) #company name
    job_title=models.CharField(max_length=100)
    job_location=models.CharField(max_length=225)
    job_package=models.IntegerField()
    job_logo=models.ImageField(upload_to='jobpost_image',null=True)
    qualification=models.CharField(max_length=225)
    options=(
        ('experience','experienced'),
        ('fresher','fresher'),
    )
    experience=models.CharField(max_length=225,choices=options,null=True)
    job_description=models.CharField(max_length=225)
    post_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.job_title


class JobApplication(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    job_title=models.ForeignKey(JobPost,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=100)
    phone=models.IntegerField()
    cv=models.FileField(upload_to='cv')
    experince=models.CharField(max_length=225)
    email=models.EmailField()
    date=models.DateTimeField(auto_now_add=True)
    liked_by=models.ManyToManyField(User,related_name='likes')

    def likes(self): # current post
        self.liked_by.all().count() 

class SavedJobs(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    job_title=models.ForeignKey(JobPost,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    

