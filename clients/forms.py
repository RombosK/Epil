from django import forms
from django.forms.widgets import SelectDateWidget
from .models import Client
from datetime import date


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['username', 'name', 'surname', 'phone', 'city', 'date_of_laser',
                  'procedure_1', 'procedure_2', 'procedure_3', 'procedure_4',
                  'procedure_5', 'procedure_6', 'procedure_7', 'procedure_8',
                  'procedure_9', 'procedure_10', 'notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Определяем начальный год
        start_year = 2022

        # Получаем текущий год
        this_year = date.today().year

        # Создаем диапазон годов от 2022 до текущего года
        year_range = range(start_year, this_year + 5)  # Включает текущий год

        # Заменяем виджет для поля date_of_laser на SelectDateWidget с указанным диапазоном годов
        self.fields['date_of_laser'].widget = SelectDateWidget(years=year_range)
