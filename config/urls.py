from django.contrib import admin
from django.urls import path, re_path
from django.urls.conf import include

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),

    re_path(r'^', include('dkea.urls')),
]
