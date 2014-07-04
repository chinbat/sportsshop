from django.db import models

class Category1(models.Model):
    sport = models.CharField(max_length=50)
    using_ball = models.BooleanField()
    def __unicode__(self):
        return self.sport

class Status1(models.Model):
    status_name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.status_name
class User1(models.Model):
    name = models.CharField(max_length=50)
    status = models.ForeignKey(Status1)
    def __unicode__(self):
        return self.name
class Post1(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True,blank=True)
    last_edited_date = models.DateTimeField(auto_now=True,blank=True)
    deleted = models.BooleanField()
    image = models.ImageField(upload_to="images/")
    posted_by = models.ForeignKey(User1)
    category = models.ForeignKey(Category1)
    post_txt = models.CharField(max_length=1000)
    def __unicode__(self):
        return self.title

class Comment1(models.Model):
    post = models.ForeignKey(Post1)
    posted_by = models.ForeignKey(User1)
    com_txt = models.CharField(max_length=200)
    def __unicode__(self):
        return self.posted_by

class Likes1(models.Model):
    post = models.ForeignKey(Post1)
    liked_by = models.ForeignKey(User1)

# Create your models here.
