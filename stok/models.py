from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

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

class RDPersonel(models.Model):
    Departments = [
        ("RD", "R&D")
    ]

    uid =models.IntegerField()
    namesurname = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    department = models.CharField(max_length=50, default="R&D")
    #manager = models.ForeignKey

    def __str__ (self):
        return self.namesurname

class Stok(models.Model):

    id = models.IntegerField(primary_key=True)
    stockname = models.CharField(max_length=50)
    birim = models.CharField(max_length=10)
    materialtype = models.CharField(max_length=15 , choices= MalzemeGruplari)
    creator=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user), default=1)
    stocknumber=models.CharField(max_length=15, default="")

    def __str__(self):
        return (self.stockname)

    #def stockcreate(self):
        #super()



from river.models.fields.state import StateField


class MyModel(models.Model):
    my_state_field = StateField()