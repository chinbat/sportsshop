from django.db import models

class Post(models.Model):
    image = models.CharField(max_length=20)
    post_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    posted_by = models.CharField(max_length=50)
    def __unicode__(self):
        return self.post_text
# Create your models here.
