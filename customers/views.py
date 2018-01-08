from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from .models import (Customer, Location, Vertical, Mode)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .forms import CustomerForm


class CustomerListView(generic.ListView):
    template_name = 'customers/customer_list.html'
    #context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Customer.objects.order_by('name')


class CustomerDetailView(generic.DetailView):
    model = Customer
    template_name = 'customers/customer_detail.html'


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Customer


class CustomerCreate(CreateView):
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('customers:list')
    # The view looks for template - customer_html.form


class CustomerUpdate(UpdateView):

    model = Customer
    fields = ['name', 'location', 'mode', 'vertical']
    success_url = reverse_lazy('customers:list')
    # The view looks for template - customer_html.form

    def __init__(self, *args, **kwargs):
        super(CustomerUpdate, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))





class CustomerDelete(DeleteView):
    model = Customer
    success_url = reverse_lazy('list')