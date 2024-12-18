from django.contrib import admin

from api.models import Test


# Register your models here.
@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_dt', 'updated_dt']
    list_display_links = ['name']
