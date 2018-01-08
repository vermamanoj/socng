from django.conf.urls import url
from . import views

app_name = 'directory'

urlpatterns = [
    # url(r'^$', views.CustomerListView.as_view(), name='index'),
    #url(r'^list_(\w+)/$', views.CustomerListView.as_view(), name='list_customer'),
    #url(r'^list_customer/$', views.CustomerListView.as_view(), name='list_customer'),
    url(r'^list/(\w+)/$', views.DirectoryListView.as_view(), name='list_directory'),
    url(r'^detail_customer/(?P<pk>[-\w]+)/$', views.CustomerDetailView.as_view(), name='detail_customer'),
    url(r'^create_customer/$', views.CustomerCreate.as_view(), name='create_customer'),
    url(r'^update_customer/(?P<pk>[-\w]+)/$', views.CustomerUpdate.as_view(), name='update_customer'),

    url(r'^list_asset/$', views.AssetListView.as_view(), name='list_asset'),
    #url(r'^detail_asset/(?P<pk>[-\w]+)/$', views.assetDetailView.as_view(), name='detail_asset'),
    url(r'^create_asset/$', views.AssetCreate.as_view(), name='create_asset'),
    url(r'^update_asset/(?P<pk>[-\w]+)/$', views.AssetUpdate.as_view(), name='update_asset'),
    url(r'^create_asset/$', views.AssetCreate.as_view(), name='create_vertical'),
    url(r'^create/(\w+)/$', views.DirectoryCreate.as_view(), name='create'),
    #url(r'^update_asset/(?P<pk>[-\w]+)/$', views.CustomerUpdate.as_view(), name='update_asset'),



    # # manage customers using ModelForm based views

    #url(r'^(?P<pk>[-\w]+)/update/$', views.CustomerUpdate.as_view(), name='customer_update'),
    # url(r'^update/(?P<pk>[-\w]+)/$', views.CustomerUpdate.as_view(), name='customer_update'),


]
