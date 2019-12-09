from django.conf.urls import url
from . import views

app_name = 'Music'
urlpatterns = [
    #Music
    url(r'^$', views.IndexView.as_view(), name='index'),

    #Music/1/
    url(r'brand/details/$', views.DetailView.as_view(), name='details'),
    url(r'brand/add/$', views.AlbumCreate.as_view(), name='album_add'),
    url(r'brand/(?P<pk>[0-9]+)$', views.AlbumUpdate.as_view(), name='album_update'),
    url(r'brand/(?P<pk>[0-9]+)$', views.AlbumDelete.as_view(), name='album_delete'),
    url(r'login/', views.Login.as_view(), name='Registration'),

]

