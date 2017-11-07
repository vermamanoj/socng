from django.conf.urls import url
from . import views



app_name = 'core'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/$', views.UserListView.as_view(), name='users'),
    url(r'^user_details/(?P<pk>\d+)/$', views.UserDetailView.as_view(), name='user-detail'),
]
