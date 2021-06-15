from django.contrib import admin
from .models import Stok
import river_admin 
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.urls import reverse
from django.utils.safestring import mark_safe



def create_river_button(obj, transition_approval):
    approve_stok_url = reverse('approve_stok', kwargs={'stok_id': obj.pk, 'next_state_id': transition_approval.transition.destination_state.pk})
    return f"""
        <input
            type="button"
            style="margin:2px;2px;2px;2px;"
            value="{transition_approval.transition.source_state} -> {transition_approval.transition.destination_state}"
            onclick="location.href=\'{approve_stok_url}\'"
        />
    """




class StockAdmin(admin.ModelAdmin):
    list_display = ['stockname','no','birim','materialtype',"Onay"]


    def get_list_display(self, request):
        self.user = request.user
        return super(StockAdmin, self).get_list_display(request)

    def Onay(self, obj):
        content = ""
        for transition_approval in obj.river.Stok_Talebi.get_available_approvals(as_user=self.user):
            content = content+ create_river_button(obj, transition_approval)

        return mark_safe(content)



admin.site.register(Stok, StockAdmin)

class StockRiverAdmin(river_admin.RiverAdmin):
    name = "Stok Kodu İş Akışı"
    icon = "mdi-ticket-account"

@classmethod
def custom_pk(cls, obj):
    return "Primary Key: %d" % obj.pk

river_admin.site.register(StockAdmin, "Stok_Talebi", StockRiverAdmin)