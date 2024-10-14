from django.db import models


class Chats(models.Model):
    message = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
