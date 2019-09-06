from django.db import models

# Create your models here.
class register(models.Model):
    name = CharField(max length = 100,)
    email = EmailField(null=True)


