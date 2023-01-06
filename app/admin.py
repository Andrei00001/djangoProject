from django.contrib import admin

# Register your models here.
from app import models

register_admin = admin.site.register


class FormAdmin(admin.ModelAdmin):
    model = models.Form
    fields = [
        'name',
        'email',
        'phone',
        'date',
        'text',
    ]
    list_display = 'name',


register_admin(models.Form, FormAdmin)
