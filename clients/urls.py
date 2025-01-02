from django.urls import path
from .views import (
    ClientListView,
    ClientDetailView,
    ClientUpdateView,
    ClientDeleteView, ClientCreateView, AccessDeniedView,
)

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),  # Список клиентов
    path('client/create/', ClientCreateView.as_view(), name='client_create'),  # Создание нового клиента
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),  # Детали клиента
    path('client/<int:pk>/edit/', ClientUpdateView.as_view(), name='client_edit'),  # Редактирование клиента
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),  # Удаление клиента
    path('access_denied/', AccessDeniedView.as_view(), name='access_denied'),  # Страница доступа запрещен
]
