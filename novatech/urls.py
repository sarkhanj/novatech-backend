from django.urls import re_path
from novatech import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^regions$',views.regionsApi),
    re_path(r'^dataset$', views.datasetApi),
    re_path(r'^records/([0-9]+)$',views.recordsApi),
    re_path(r'^ml/([0-9]+)$', views.mlApi),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)