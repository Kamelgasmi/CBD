from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = RichTextField()
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name