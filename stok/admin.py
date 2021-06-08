from django.contrib import admin
from .models import Stok, RDPersonel


class RDPersonelAdmin(admin.ModelAdmin):
    list_display = ['uid', 'namesurname']


class StockAdmin(admin.ModelAdmin):
    list_display = ['stockname','id','birim','materialtype']


admin.site.register(Stok, StockAdmin)
admin.site.register(RDPersonel, RDPersonelAdmin)
