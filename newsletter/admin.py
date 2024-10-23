from django.contrib import admin
from .models import Opportunity
from .forms import OpportunityModelForm

class OpportunityAdmin(admin.ModelAdmin):
    list_display = ["email", "name", "created_on", "updated_on"]
    # list_display_links = ["name"]
    list_filter = ["created_on", "updated_on"]
    list_editable = ["name"]
    search_fields = ["email", "name"]
    # class Meta:
    #     model = Opportunity
    form = OpportunityModelForm

admin.site.register(Opportunity, OpportunityAdmin)