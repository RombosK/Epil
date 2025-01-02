from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {"blank": True, "null": True}


class BaseModel(models.Model):  # base class should subclass 'django.db.models.Model'
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"), editable=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="_(updated_at)", editable=False)
    deleted = models.BooleanField(default=False, verbose_name=_("deleted"))

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


class Client(BaseModel):
    username = models.CharField(max_length=100, verbose_name='Запись как в телефоне')
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = models.CharField(max_length=100, verbose_name='Телефон', unique=True)
    city = models.CharField(max_length=100, verbose_name='Город')
    date_of_laser = models.DateField(verbose_name='Дата первой процедуры')
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    procedure_1 = models.CharField(max_length=1000, verbose_name="Процедура 1", **NULLABLE)
    procedure_2 = models.CharField(max_length=1000, verbose_name="Процедура 2", **NULLABLE)
    procedure_3 = models.CharField(max_length=1000, verbose_name="Процедура 3", **NULLABLE)
    procedure_4 = models.CharField(max_length=1000, verbose_name="Процедура 4", **NULLABLE)
    procedure_5 = models.CharField(max_length=1000, verbose_name="Процедура 5", **NULLABLE)
    procedure_6 = models.CharField(max_length=1000, verbose_name="Процедура 6", **NULLABLE)
    procedure_7 = models.CharField(max_length=1000, verbose_name="Процедура 7", **NULLABLE)
    procedure_8 = models.CharField(max_length=1000, verbose_name="Процедура 8", **NULLABLE)
    procedure_9 = models.CharField(max_length=1000, verbose_name="Процедура 9", **NULLABLE)
    procedure_10 = models.CharField(max_length=1000, verbose_name="Процедура10", **NULLABLE)
    notes = models.TextField(verbose_name="Примечания", **NULLABLE)

    def __str__(self) -> str:
        return f"{self.pk} {self.name} {self.surname} {self.phone} {self.city} {self.date_of_laser} {self.notes}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
