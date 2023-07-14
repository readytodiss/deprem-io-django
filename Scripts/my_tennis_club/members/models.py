from django.db import models

class GidaIhtiyaci(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    human_count = models.IntegerField()
    address = models.TextField()
    address_description = models.TextField()
    physical_info = models.CharField(max_length=10)
    tweet_link = models.URLField()
   
    def __str__(self):
        return self(fullname,email,phone,human_count,address,address_description,physical_info,tweet_link)