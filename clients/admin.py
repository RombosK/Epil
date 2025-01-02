from django.contrib import admin

from .models import Client


@admin.register(Client)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'surname', 'phone', 'city', 'date_of_laser', 'notes')
    list_per_page = 10
    list_filter = ('username', 'name', 'surname', 'phone', 'city', 'date_of_laser', 'notes')
    search_fields = ('username', 'name', 'surname')
    show_full_result_count = False

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

