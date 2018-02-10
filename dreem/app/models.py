from django.db import models

class User(models.Model):
    name = models.CharField()


class Device(models.Model):
    name = models.CharField()
    users = models.ManyToManyField(Users)


class Record(models.Model):
    file = models.CharField()	
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
