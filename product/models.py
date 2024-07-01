from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.title