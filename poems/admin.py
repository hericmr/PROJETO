from django.contrib import admin
from .models import Poema
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Poema, SummerAdmin)