from django.conf.urls import url
from . import views

app_name = 'customers'

urlpatterns = [
    url(r'^$', views.CustomerListView.as_view(), name='index'),
    url(r'^list/$', views.CustomerListView.as_view(), name='list'),
    url(r'^details/(?P<pk>[-\w]+)/$', views.CustomerDetailView.as_view(), name='details'),
    # manage customers using ModelForm based views
    url(r'^create/$', views.CustomerCreate.as_view(), name='customer_create'),
    #url(r'^(?P<pk>[-\w]+)/update/$', views.CustomerUpdate.as_view(), name='customer_update'),
    url(r'^update/(?P<pk>[-\w]+)/$', views.CustomerUpdate.as_view(), name='customer_update'),
    url(r'^(?P<pk>\[-\w])/delete/$', views.CustomerDelete.as_view(), name='customer_delete'),

]
