from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    pub_date = models.DateTimeField()
    
    post = models.TextField()
    image = models.ImageField(upload_to ='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.post[:100]
    
    def date(self):
        return self.pub_date.strftime('%a %d %b %Y ')