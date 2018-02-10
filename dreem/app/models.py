from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)


class Device(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(User)


class Record(models.Model):
    file = models.CharField(max_length=50)	
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
