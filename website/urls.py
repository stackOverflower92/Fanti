from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^gallery/(?P<album_id>[0-9]+)/$', views.album, name='album'),
    url(r'^gallery/(?P<album_id>[0-9]+)/(?P<image_id>[0-9]+)/$', views.image, name='image'),
    url(r'^tornitura/$', views.tornitura, name='tornitura'),
    url(r'^fresatura/$', views.fresatura, name='fresatura'),
    url(r'^tornitura/(?P<machine_id>[0-9]+)/$', views.machine, name='tmachine'),
    url(r'^fresatura/(?P<machine_id>[0-9]+)/$', views.machine, name='fmachine'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
