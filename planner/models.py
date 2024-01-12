from django.contrib.auth.models import AbstractUser
from django.db import models
#from django.utils import timezone
#from datetime import date, timedelta
from datetime import datetime, timedelta, date
from taggit.managers import TaggableManager

# Create your models here.
class User(AbstractUser):
    pass
    about = models.TextField(blank=True, null=True)
    #joined_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(blank=True, null=True, upload_to='images/')

    def __str__(self):
        return f"{self.username}"

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "posts")
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=300)
    location = models.CharField(max_length=150)
    photo = models.ImageField(blank=True, null=True, upload_to='images/')
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="likes")
    tags = TaggableManager()

    class Meta:
        ordering = ['-timestamp']

    def post_time(self):
        return humanize.naturaltime(self.timestamp)

 
    def __str__(self):
        return f"Posted by: {self.author} with post: {self.body} On: {self.timestamp} with: {self.likes.count()} likes"


class Trip(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "trip")
    destination = models.CharField(max_length=150)
    purpose = models.TextField()
    #trip_date =  models.DateTimeField()
    departure =  models.DateField(default=date.today)
    arrival = models.DateField(default=date.today() + timedelta(days=3))
    class Meta:
        ordering = ['-departure']

    @property
    def is_past_due(self):
       return date.today() > self.arrival

    def __str__(self):
        return f"{self.owner} travels to {self.destination} for {self.purpose} on {self.departure} and returns on {self.arrival}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    post = models.ForeignKey(Post, on_delete =models.CASCADE, related_name="comment")
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    timestamp = models.DateTimeField(auto_now=True)
    #hidden = models.CharField(max_length=255, blank=True)  # To get a comment ID in the modelForm

    class Meta:
      ordering = ["-timestamp"]

   
    def __str__(self):
        return f"{self.content}"


