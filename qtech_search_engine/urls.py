from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from qtech_search_engine.views import (
    HomeView,
    SearchView,
    TestView
)

app_name = 'qtech_search_engine'

urlpatterns = [
    path('', HomeView, name='home'),
    path('search/', SearchView, name="search"),
    path('test/', TestView, name="test")
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
