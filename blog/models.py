from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)    
    cover = models.ImageField(upload_to='images/',default='null')
    body1 = models.TextField(default='',blank=True)
    image1 = models.ImageField(upload_to='images/',default='null')
    body2 = models.TextField(default='',blank=True)
    image2 = models.ImageField(upload_to='images/',default='null')
    body3 = models.TextField(default='',blank=True)
    image3 = models.ImageField(upload_to='images/',default='null')
    body4 = models.TextField(default='',blank=True)
    image4 = models.ImageField(upload_to='images/',default='null')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    