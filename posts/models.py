from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    
    titolo = models.CharField(max_length = 120,default=None)
    contenuto = models.TextField(default=None,blank=True,null=True)
    data = models.DateTimeField(auto_now = False, auto_now_add = True)
    slug = models.SlugField()    


    def __str__(self):
        return self.titolo

    #best practice per ottenere url post singolo
    def get_absolute_url(self):
        return reverse("singolo", kwargs = {"id": self.id, "slug": self.slug})
    
class Comment(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments', blank=False, null=True)
    titolo = models.CharField(max_length=200,default=None)
    contenuto = models.TextField(default=None,blank=True,null=True)
    data = models.DateField(auto_now = False, auto_now_add = True)
    approved_comment = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("add_comment_to_post", kwargs = {"pk": pk.pk})


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.titolo

# Create your models here.
