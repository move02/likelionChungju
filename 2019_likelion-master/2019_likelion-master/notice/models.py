from django.db import models
from django.forms import ValidationError

class Post(models.Model):
    title = models.CharField(max_length=50, blank=False)
    content = models.TextField (blank=False, null=True)
    pub_date= models.DateTimeField(auto_now_add=True)
    importance = models.BooleanField (blank=False, default=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post',on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=15)
    text = models.TextField(blank=True, null=False)
    #password = models.CharField(validators=[])

    def __str__(self):
        return self.text       


