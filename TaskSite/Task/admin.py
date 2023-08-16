from django.contrib import admin
from .models import *
class StatusAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}
class TaskAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}

admin.site.register(Task,TaskAdmin)
admin.site.register(Message)
admin.site.register(Status,StatusAdmin)