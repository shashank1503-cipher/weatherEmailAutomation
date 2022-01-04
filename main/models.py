from django.db import models

# Client Details Table.
class ClientDetails(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    temperature = models.IntegerField()
    timeRequested = models.DateTimeField()

    def __str__(self) -> str:
        return self.username
        