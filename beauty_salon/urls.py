# project/urls.py

from django.contrib import admin
from django.urls import path, include
from clients.views import ClientListView, AccessDeniedView  # Импортируем представление списка клиентов

urlpatterns = [
    path('adminboard/', admin.site.urls),
    path('', ClientListView.as_view(), name='client_list'),  # Главная страница с выводом списка клиентов
    path('clients/', include('clients.urls')),  # Подключаем URL-адреса приложения clients
]
