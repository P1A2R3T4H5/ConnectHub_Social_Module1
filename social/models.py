from django.conf import settings
from django.db import models
class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="profile")
    bio=models.CharField(max_length=180,blank=True)
    avatar=models.ImageField(upload_to="avatars/",blank=True,null=True)
    website=models.URLField(blank=True)
    def __str__(self): return self.user.username
class Follow(models.Model):
    follower=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="following_links")
    following=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="follower_links")
    class Meta: constraints=[models.UniqueConstraint(fields=["follower","following"],name="unique_follow_pair")]
class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="posts")
    caption=models.CharField(max_length=2200,blank=True)
    image=models.ImageField(upload_to="posts/",blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=["-created_at"]
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    text=models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=["created_at"]
class Like(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="likes")
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    class Meta: constraints=[models.UniqueConstraint(fields=["post","user"],name="unique_post_like")]
