from django.db import models

from django.db import models

class Distrik(models.Model):
    id_distrik = models.AutoField(primary_key=True)
    nama_distrik = models.CharField(max_length=30)

    def __str__(self):
        return self.nama_distrik

class Kampung(models.Model):
    id_kampung = models.AutoField(primary_key=True)
    distrik = models.ForeignKey(Distrik, on_delete=models.CASCADE)
    nama_kampung = models.CharField(max_length=30)

    def __str__(self):
        return self.nama_kampung