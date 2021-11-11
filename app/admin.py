from django.contrib import admin

# Register your models here.
from app.models import Student


@admin.register(Student)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'age', 'grade')
