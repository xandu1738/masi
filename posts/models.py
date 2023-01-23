from django.db import models

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.user', related_name='posts', on_delete=models.CASCADE)
    body = models.TextField()
    # image
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']
