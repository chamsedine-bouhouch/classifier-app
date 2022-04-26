from django.urls import path  
from .views import image_request ,test
  
app_name = 'image_app'  
urlpatterns = [
    path('', image_request, name = "image-request"),
    path('test',test)
    ]