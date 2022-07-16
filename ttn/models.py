
from enum import unique
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title=models.TextField(max_length=150,unique=True)
    content=models.TextField(max_length=1500)
    created=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="posted_by")
    updated_on=models.DateTimeField(auto_now=True)
    description=models.TextField(max_length=150)
    place=models.TextField()
    img=models.ImageField(null=False,blank=False,upload_to="uploads//",unique=True)

    class Meta:
        ordering=['-created']

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.img.delete()
        super().delete()


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return '%s - %s' %(self.post.title, self.user.username)

