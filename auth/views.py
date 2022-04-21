from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'home.html')
# def login(request):
#     return render(request, 'auth/login.html')
# def register(request):
#     return HttpResponse("Register Page")


# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
        
#     else:
#         # Return an 'invalid login' error message.