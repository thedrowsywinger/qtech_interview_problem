from django.db import models
# Create your models here.

class KeywordDescriptionModel(models.Model):
    keyword = models.CharField(max_length = 100)
    description = models.CharField(max_length = 255)
    times_searched = models.IntegerField()
    time = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.keyword

class AllUsers(models.Model):
    username = models.CharField(max_length = 100)
    user_sid = models.CharField(max_length = 100)
    keyword = models.ManyToManyField(KeywordDescriptionModel)

    def __str__(self):
        return self.user_sid
