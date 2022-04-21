from django.urls import path

from . import views
# Namespacing url
app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='home')
]