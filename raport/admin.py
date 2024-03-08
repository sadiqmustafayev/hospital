from django.contrib import admin
from .models import AnalizRaport


@admin.register(AnalizRaport)
class AnalizRaportAdmin(admin.ModelAdmin):
  list_display = ('id', 'name_surname', 'date')
