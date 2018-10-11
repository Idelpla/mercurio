from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import StatementForm
from .models import Statement


class StatementList(LoginRequiredMixin, ListView):
    model = Statement
    template_name = 'statement/list.html'


class StatementNew(LoginRequiredMixin, CreateView):
    model = Statement
    form_class = StatementForm
    template_name = 'standard_form.html'
    success_url = reverse_lazy('statements:list')
