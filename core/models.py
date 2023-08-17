from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    description = models.TextField(null=False)
    image_url = models.URLField(null=False)
    puntaje = models.IntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    actor_1 = models.CharField(max_length=100)
    actor_2 = models.CharField(max_length=100)
    reseña = models.TextField()
    def __str__(self):
        return self.title