# clients/forms.py
#
# from django import forms
# from .models import Client
#
#
# class ClientForm(forms.ModelForm):
#     class Meta:
#         model = Client
#         fields = ['username', 'name', 'surname', 'phone', 'city', 'date_of_laser',
#                   'procedure_1', 'procedure_2', 'procedure_3', 'procedure_4',
#                   'procedure_5', 'procedure_6', 'procedure_7', 'procedure_8',
#                   'procedure_9', 'procedure_10', 'notes']

# forms.py
from django import forms
from django.forms.widgets import SelectDateWidget
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['username', 'name', 'surname', 'phone', 'city', 'date_of_laser',
                  'procedure_1', 'procedure_2', 'procedure_3', 'procedure_4',
                  'procedure_5', 'procedure_6', 'procedure_7', 'procedure_8',
                  'procedure_9', 'procedure_10', 'notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Заменяем виджет для поля date_of_laser на SelectDateWidget
        self.fields['date_of_laser'].widget = SelectDateWidget()
