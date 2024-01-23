from django.db import models

# Create your models here.
class Note(models.Model):
    """ The note model """
    body = models.TextField(max_length=1000, null=True)
    updated = models.DateField(auto_now=True, null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]
    
