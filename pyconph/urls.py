from django.conf.urls import include, url
from django.contrib import admin

from pyconph.program.views import cfp

urlpatterns = [
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^cfp/$', cfp, name='cfp'),
    url(r'^admin/', admin.site.urls),
]
