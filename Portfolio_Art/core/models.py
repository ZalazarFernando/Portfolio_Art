from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)

    # FK hacia sí mismo
    follow = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    likes = models.IntegerField()
    post_date = models.DateTimeField()

class Hashtag(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    name_hashtag = models.CharField(max_length=50)