from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    id=models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.id}-{self.title}-{self.author}"
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
        	url = ''
        return url
    @property
    def no_of_likes(self):
        likes=self.like_set.all().count()
        if likes:
            return likes
        else:
            return 0
    # @property
    # def liked_or_not(self):
        




class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    picture = models.ForeignKey(Post,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)