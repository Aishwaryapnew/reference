
        
from django.db import models

class reference(models.Model):
    id = models.AutoField(primary_key=True)  
    referencesis = models.CharField(max_length=255)
    coursecode = models.TextField()  # Provide a default value for existing rows
    academic_yr = models.CharField(max_length=9)   # Default year for existing rows

    class Meta:
        db_table = 'reference'
