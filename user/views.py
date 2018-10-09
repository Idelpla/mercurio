from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, UpdateView

from .forms import LoginFormHelper, ElectronicAddressForm
from django.urls import reverse_lazy

User = get_user_model()


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'user/dashboard.html'


class Login(LoginView):
    template_name = 'standard_form.html'

    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)
        context['title'] = 'Login'
        context['form_helper'] = LoginFormHelper()
        return context


class ElectronicAddress(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ElectronicAddressForm
    template_name = 'standard_form.html'
    success_url = reverse_lazy('users:dashboard')

    def get_object(self, queryset=None):
        self.kwargs['pk'] = self.request.user.pk
        return super(ElectronicAddress, self).get_object(queryset)

