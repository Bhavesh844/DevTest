from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class upload_file(models.Model):
    
        file=models.FileField(upload_to='media/', validators=[FileExtensionValidator(['csv','xlsx'])],error_messages='Please upload valid file')
         
    
    