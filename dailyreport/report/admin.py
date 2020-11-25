from django.contrib import admin
from .models import Work
from .models import Profile

# Register your models here.
class DesignPostAdmin(admin.ModelAdmin):
    
    list_display = ["date","content","create_at"]
    fields = ["date","content","create_at"]


admin.site.register(Work,DesignPostAdmin)
admin.site.register(Profile)
