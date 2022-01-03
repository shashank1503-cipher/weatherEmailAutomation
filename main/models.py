from django.db import models

# Create your models here.
class ClientDetails(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    temperature = models.IntegerField()
    timeRequested = models.DateTimeField()

    def __str__(self) -> str:
        return self.username
        