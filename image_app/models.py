from django.db import models

class UploadImage(models.Model):  
    patient = models.CharField(max_length=200)  
    image = models.ImageField(upload_to='images')  
  
    def __str__(self):  
        return self.caption  
class Result(models.Model):
    image = models.OneToOneField(
        UploadImage,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    result = models.CharField(max_length=20)  
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):  
        return self.result  