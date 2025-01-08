from django.contrib.auth.mixins import UserPassesTestMixin

from django.http import JsonResponse, request
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from django.urls import reverse_lazy
from .models import Client
from .forms import ClientForm  # Импортируем форму для клиента
from django.db.models import Q  # Импортируем Q для выполнения сложных запросов


class SuperuserRequiredMixin(UserPassesTestMixin):
    """Mixin для проверки суперпользователя."""

    def test_func(self):
        return self.request.user.is_superuser


class AccessDeniedView(TemplateView):
    template_name = 'access_denied.html'


class ClientCreateView(SuperuserRequiredMixin, CreateView):
    """Создание нового клиента."""
    model = Client
    form_class = ClientForm
    template_name = 'client_create.html'

    def get_success_url(self):
        return reverse_lazy('client_list')  # Перенаправление на список клиентов после успешного создания


class ClientListView(SuperuserRequiredMixin, ListView):
    """Отображение списка клиентов."""
    paginate_by = 50   # Количество клиентов на странице
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'clients'

    def get_queryset(self):
        queryset = Client.objects.filter(deleted=False)  # Показываем только не удаленных клиентов
        search_query = self.request.GET.get('search', '')  # Получаем значение из поля поиска

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(surname__icontains=search_query) |
                Q(phone__icontains=search_query) |
                Q(city__icontains=search_query) |
                Q(username__icontains=search_query)
            )

        return queryset.order_by('id')

    def get(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Проверка на AJAX-запрос
            clients = self.get_queryset()
            client_data = [
                {
                    'id': client.pk,
                    'name': client.name,
                    'surname': client.surname,
                    'phone': client.phone,
                    'city': client.city,
                }
                for client in clients
            ]
            return JsonResponse(client_data, safe=False)
        else:
            return super().get(request, *args, **kwargs)


class ClientDetailView(SuperuserRequiredMixin, DetailView):
    """Отображение информации о конкретном клиенте."""
    model = Client
    template_name = 'client_detail.html'
    context_object_name = 'client'

    def get_queryset(self):
        return Client.objects.filter(deleted=False)  # Показываем только не удаленных клиентов


class ClientUpdateView(SuperuserRequiredMixin, UpdateView):
    """Редактирование информации о клиенте."""
    model = Client
    form_class = ClientForm
    template_name = 'client_edit.html'

    def get_success_url(self):
        return reverse_lazy('client_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        """Обработка валидной формы."""
        return super().form_valid(form)

    def form_invalid(self, form):
        """Обработка невалидной формы."""
        return super().form_invalid(form)


class ClientDeleteView(SuperuserRequiredMixin, DeleteView):
    """Удаление клиента (логическое)."""
    model = Client
    template_name = 'client_delete.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()  # Логическое удаление (установка поля deleted в True)
        return redirect('client_list')

    def get_queryset(self):
        return Client.objects.filter(deleted=False)  # Показываем только не удаленных клиентов

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client'] = self.get_object()
        return context
