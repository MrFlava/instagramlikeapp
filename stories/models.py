from PIL import Image
from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model

# Create your models here.


class Story(models.Model):
    image = models.ImageField(upload_to="story_images")
    date = models.DateTimeField("date published", default=datetime.now())
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.author) + ':   ' + str(self.date)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 1000 or img.width > 1000:
            output_size = (1000, 1000)
            img.thumbnail(output_size)
            img.save(self.image.path)

    objects = models.Manager()


class WatchedStory(models.Model):
    story = models.ForeignKey(Story, related_name='watchedstories', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), related_name='watchedstories', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + ':   ' + str(self.story)

    objects = models.Manager()
