from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.views import generic
from .models import (Customer, Vertical, Location, Mode)
from .models import (Asset, AssetAction, AssetAttribute, AssetType, AssetFunction, AssetActionOn)
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms


class CustomerCreate(CreateView):
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('directory:list_customer')
    # The view looks for template - customer_html.form


class CustomerUpdate(UpdateView):
    model = Customer
    fields = ['name', 'location', 'mode']
    success_url = reverse_lazy('directory:list_customer')
    # The view looks for template - customer_html.form


class CustomerDelete(DeleteView):
    model = Customer
    success_url = reverse_lazy('list')


class AssetCreate(CreateView):
    # Override base get_form class to change widget for password field
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['password'].widget = forms.PasswordInput()
        return form

    model = Asset
    fields = '__all__'
    success_url = reverse_lazy('directory:list_asset')
    # The view looks for template - asset_html.form


class AssetUpdate(UpdateView):
    # Override base get_form class to change widget for password field
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['password'].widget = forms.PasswordInput()
        return form

    model = Asset
    password = forms.CharField(widget=forms.PasswordInput)
    fields = '__all__'
    success_url = reverse_lazy('directory:list_asset')
    # The view looks for template - asset_html.form


class AssetDelete(DeleteView):
    model = Asset
    success_url = reverse_lazy('list_asset')


class AssetListView(generic.ListView):
    context_object_name = 'directory_list'
    model = Asset
    model_name = "Asset"

    fields = ['name', 'customer']

    def get_queryset(self):
        """Return the last five published questions."""
        return self.model.objects.order_by('name')

    template_name = 'directory/directory_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['model_name'] = self.model_name
        context['fields'] = self.fields
        context['url'] = reverse('directory:create_' + str.lower(self.model_name))

        return context


class CustomerListView(generic.ListView):
    context_object_name = 'directory_list'
    fields = ['name', 'vertical', 'location', 'mode']
    model = Customer
    model_name = "Customer"

    def get_queryset(self):
        """Return the last five published questions."""
        print("args", self.args)
        return self.model.objects.order_by('name')

    template_name = 'directory/directory_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['model_name'] = self.model_name
        context['fields'] = self.fields
        context['url'] = reverse('directory:create_' + str.lower(self.model_name))
        return context


class DirectoryListView(generic.ListView):
    # This is a single view to list all models
    context_object_name = 'directory_list'
    template_name = 'directory/directory_list.html'
    fields = []
    model = ''
    model_name = ''

    def get_queryset(self):
        model_dict = {
            "vertical": Vertical,
            "customer": Customer,
            "location": Location,
            "mode": Mode,
            "asset": Asset,

        }
        self.model_name = self.args[0]
        self.model = model_dict[self.args[0]]

        return self.model.objects.order_by('name')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['model_name'] = self.model_name
        context['fields'] = self.fields
        context['url'] = reverse('directory:create', args=[self.model_name])

        return context


class CustomerDetailView(generic.DetailView):
    model = Customer
    template_name = 'directory/customer_detail.html'


class DirectoryCreate(CreateView):
    #context_object_name = 'directory_list'
    template_name = 'directory/asset_form.html'
    fields = []
    model = Mode
    model_name = ''

    def get_queryset(self):
        queryset = super().get_queryset()
        model_dict = {
            "vertical": Vertical,
            "customer": Customer,
            "location": Location,
            "mode": Mode,
            "asset": Asset,

        }
        self.model_name = self.args[0]
        self.model = model_dict[self.args[0]]

        return self.queryset.all()

    def get_form(self, form_class=None):
        form = super(DirectoryCreate, self).get_form(form_class)
        model_dict = {
            "vertical": Vertical,
            "customer": Customer,
            "location": Location,
            "mode": Mode,
            "asset": Asset,

        }
        self.model_name = self.args[0]
        #self.model = model_dict[self.args[0]]
        self.model = Mode
        return form

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['model_name'] = self.model_name
    #     context['fields'] = self.fields
    #     context['url'] = reverse('directory:create_' + str.lower(self.model_name))
    #     return context

