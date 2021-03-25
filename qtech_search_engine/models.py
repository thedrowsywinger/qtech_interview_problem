from django.db import models
# Create your models here.


class AllUsers(models.Model):
    username = models.CharField(max_length = 100)
    user_sid = models.CharField(max_length = 100)

    def __str__(self):
        return self.username

class KeywordDescriptionModel(models.Model):
    keyword = models.CharField(max_length = 100)
    description = models.CharField(max_length = 255)
    times_searched = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField(AllUsers)

    def __str__(self):
        return self.keyword