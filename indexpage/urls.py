from django.urls import path
from indexpage.views import *


urlpatterns = [
    path('', index_view, name='index'),
]
