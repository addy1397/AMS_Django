from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^ticketing/', include('ticketing.urls')),
    url(r'^admin/', admin.site.urls),
]
