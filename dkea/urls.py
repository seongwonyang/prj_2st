from django.urls import re_path
from .views import *

app_name = 'dkea'

urlpatterns = [
    re_path(r'^$', DkeaMain, name='main'),
    re_path(r'^list/(?P<list>c\d+)/$', DkeaListView, name='list'),
    re_path(r'^detail/(?P<detail>\d+)/$', DkeaDetailView, name='detail')
]