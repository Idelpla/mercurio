from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy

from .forms import StatementForm, AttachmentFormSet, AttachmentFormSetHelper
from .models import Statement

from django.http import HttpResponseRedirect

from django.core.exceptions import PermissionDenied


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

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        formset = AttachmentFormSet(self.request.POST, self.request.FILES)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        form.instance.owner = self.request.user
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset):
        helper = AttachmentFormSetHelper()
        return self.render_to_response(self.get_context_data(form=form, formset=formset, formset_helper=helper))

    def get_success_url(self):
        return reverse_lazy('statements:detail', kwargs={'pk': self.object.pk})


class StatementDetail(LoginRequiredMixin, DetailView):
    model = Statement
    template_name = 'statement/detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner != self.request.user:
            raise PermissionDenied
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
