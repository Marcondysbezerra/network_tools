from django.db import models


class IpExterno(models.Model):
    ip = models.CharField(max_length=255)
    porta = models.IntegerField()
