from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    image = models.ImageField()
    description = models.TextField()
    date = models.DateTimeField("date published", default=datetime.now())
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.description

    objects = models.Manager()


# class Preference(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     value = models.IntegerField()
#     date = models.DateTimeField(default=datetime.now())
#
#     def __str__(self):
#         return str(self.user) + ':   ' + str(self.post) + ':' + str(self.value)
#
#     class Meta:
#         unique_together = ("user", "post", "value")
#
#     objects = models.Manager()
