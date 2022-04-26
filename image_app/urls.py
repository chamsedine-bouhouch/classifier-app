from django.urls import path  
from .views import image_request  
  
app_name = 'image_app'  
urlpatterns = [
    path('', image_request, name = "image-request")  
    ]