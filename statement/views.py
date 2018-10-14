from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy

from .forms import StatementForm, AttachmentFormSet, AttachmentFormSetHelper
from .models import Statement

from django.http import HttpResponseRedirect


class StatementList(LoginRequiredMixin, ListView):
    model = Statement
    template_name = 'statement/list.html'
    context_object_name = 'statements'

    def get_queryset(self):
        return super(StatementList, self).get_queryset().filter(owner=self.request.user)


class StatementNew(LoginRequiredMixin, CreateView):
    model = Statement
    form_class = StatementForm
    template_name = 'standard_form.html'

    def get_context_data(self, **kwargs):
        context = super(StatementNew, self).get_context_data(**kwargs)
        context['formset'] = AttachmentFormSet()
        context['formset_helper'] = AttachmentFormSetHelper()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('statements:detail', kwargs={'pk': self.object.pk})


class StatementDetail(LoginRequiredMixin, DetailView):
    model = Statement
    template_name = 'statement/detail.html'
