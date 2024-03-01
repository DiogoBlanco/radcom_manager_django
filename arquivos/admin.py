from django.contrib import admin
from .models import Files


class FilesAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'updated_at',
                    'customer', 'title', 'backup_pabx', 'backup_rb']


admin.site.register(Files)
