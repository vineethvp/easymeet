from django.db import models
from django.utils import timezone
# Create your models here.

class Meetup(models.Model):
    cre_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')

    def create_meetup(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
