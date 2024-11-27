from django.db import models

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
