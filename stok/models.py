from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from river.models.fields.state import StateField


MalzemeGruplari= (
        ('AG.A1010','NVR-DVR'),
        ('AG.A1020', 'MONITOR'),
        ('AG.A1010', 'KAMERA'),
)

Projeler = (
    ('Izmir','VMS')

)

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]



class Stok(models.Model):

    no = models.IntegerField(primary_key=True)
    stockname = models.CharField(max_length=50)
    birim = models.CharField(max_length=10)
    materialtype = models.CharField(max_length=15 , choices= MalzemeGruplari)
    creator=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user), default=1)
    stocknumber=models.CharField(max_length=15, default="", unique=True)
    status = models.BooleanField(default=True)
    Stok_Talebi = StateField(editable=False)

    def __str__(self):
        return (self.stockname)

    def create(self,materialtype):
        pass

    def natural_key(self):
        return self.no

    def get_changelist(self, request, **kwargs):
        """
        Return the ChangeList class for use on the changelist page.
        """
        from django.contrib.admin.views.main import ChangeList
        return ChangeList 

    