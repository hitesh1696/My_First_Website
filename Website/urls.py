
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('Music.urls')),
    url(r'^Music/Home',include('Music.urls')),
]
