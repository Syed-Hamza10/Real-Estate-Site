from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

fs = FileSystemStorage(location=settings.MEDIA_ROOT)

class PropertyCategory(models.Model):
    class Meta:
        verbose_name_plural = "Property Categories"
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name 

class Property(models.Model):


    class Meta:
        verbose_name_plural = "Properties"
    purpose_choices = [
        ('For Rent', 'For Rent'),
        ('For Sale','For Sale')
    ]
    negotiable_choices = [('Y','YES'),('N','NO')]
    title = models.CharField(max_length=50) 
    description = models.TextField()    
    address = models.CharField(max_length=250)
    area = models.CharField(max_length=250)
    category = models.ForeignKey(PropertyCategory, on_delete=models.CASCADE)
    purpose = models.CharField(choices=purpose_choices, max_length=15)
    price = models.IntegerField()
    main_image = models.ImageField()
    image_2 = models.ImageField(blank=True)
    image_3 = models.ImageField(blank=True)
    image_4 = models.ImageField(blank=True)
    is_negotiable = models.CharField(max_length=3, choices=negotiable_choices, default='N')

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        print(f"Data updated for {self.title}")
        super().save(*args, **kwargs)
    
class PropertyFeature(models.Model):
    class Meta:
        verbose_name_plural = "Property Features"
        

    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=40)
    feature_value = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.feature_name 
