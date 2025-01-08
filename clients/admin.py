from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    # Поля, отображаемые в списке клиентов
    list_display = ('username', 'name', 'surname', 'phone', 'city', 'date_of_laser', 'notes')

    # Количество клиентов на странице
    list_per_page = 30  # Пагинация по умолчанию

    # Фильтры для боковой панели
    list_filter = ('username', 'name', 'surname', 'phone', 'city', 'date_of_laser')

    # Поля для поиска
    search_fields = ('username', 'name', 'surname')

    # Отключение отображения полного количества результатов (по желанию)
    show_full_result_count = True

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
