from django.db import models
from django.contrib import admin

# Create your models here.
#lets make a class for taged objects
class Tag(models.Model):
    rfid_tag = models.CharField(max_length=35,unique=True,
                                verbose_name="RFID Tag id")
    name = models.CharField(max_length=200,blank=True,null=True)
    enabled = models.BooleanField(default=True)
    
    last_seen = models.DateTimeField(blank=True,null=True)
    
    user_comment = models.TextField(max_length=500,blank=True,null=True)
    
    #optional image for the item
    image = models.ImageField(upload_to='tag_images',blank=True,null=True)
    
    def __unicode__(self):
        return self.rfid_tag
    
    
admin.site.register(Tag)