from django.conf.urls import include, url
from django.contrib import admin

from pyconph.program.views import cfp, cfp_thanks

urlpatterns = [
    url(r'^cfp/$', cfp, name='cfp'),
    url(r'^cfp/thanks/$', cfp_thanks, name='cfp_thanks'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', admin.site.urls),
]
