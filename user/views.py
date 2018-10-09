from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .forms import LoginFormHelper


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'user/dashboard.html'


class Login(LoginView):
    template_name = 'standard_form.html'

    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)
        context['title'] = 'Login'
        context['form_helper'] = LoginFormHelper()
        return context
