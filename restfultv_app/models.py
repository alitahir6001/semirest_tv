from django.db import models

# Create your models here.

class show_manager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['title']) < 3:
            errors['title'] = "Title is too short!"
        
        if len(postData['network']) < 3:
            errors['network'] = "Network length is too short!"

        if len(postData['release_date']) == 0:
            errors['release_date'] = "release_date length is too short!"

        if len(postData)['description'] == 0:
            errors['description'] = "There is no description listed!"
        
        return errors



class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = show_manager()