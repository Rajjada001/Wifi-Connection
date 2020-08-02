from django.db import models

# Create your models here.


class ConnectToWifi(models.Model):
    con = models.CharField(max_length=250)
    p = models.CharField(max_length=25)

    def __str__(self):
        return self.con
