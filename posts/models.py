from PIL import Image
from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
# Create your models here.


class Post(models.Model):
    image = models.ImageField(upload_to="post_images")
    description = models.TextField()
    date = models.DateTimeField("date published", default=datetime.now())
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,  blank=True)

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 1000 or img.width > 1000:
            output_size = (1000, 1000)
            img.thumbnail(output_size)
            img.save(self.image.path)

    objects = models.Manager()


class Like(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,  blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.user) + ':   ' + str(self.post) + ':' + str(self.date)

    class Meta:
        unique_together = ("user", "post")

    objects = models.Manager()


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,  blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now())
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    body = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return str(self.user) + ':   ' + str(self.post) + ':' + str(self.body) + ':   ' + str(self.date)
