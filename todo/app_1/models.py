from django.db import models

# Create your models here.
class todos(models.Model):
    title = models.CharField(max_length=50)
    discription = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title