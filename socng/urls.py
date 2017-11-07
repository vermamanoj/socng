from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.views.generic import RedirectView



urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/core/'), name='home'),
    url(r'^admin/', admin.site.urls),


]

urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^core/', include('core.urls')),
]
