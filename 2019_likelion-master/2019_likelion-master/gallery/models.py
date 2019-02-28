from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=50, blank=False)
    content = models.TextField (blank=False, null=True)
    image = models.ImageField(upload_to='images/')
    pub_date= models.DateTimeField(auto_now_add=True)


    def summary(self):
        return self.content[:10]
        
    def __str__(self):
        return self.title