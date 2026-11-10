from django.contrib import admin
from .models import Tutor

# Register your models here.

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'person')
    search_fields = ('person__name', 'person__cpf')