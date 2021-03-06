from django.shortcuts import redirect, render  
from image_app.forms import UserImageForm  
from .models import UploadImage ,Result
  
def image_request(request):  
    if request.method == 'POST':  
        form = UserImageForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
            print(form)
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
            q= Result(image=img_object, result="benin")
            q.save()
  
            return render(request, 'image_form.html', {'form': form, 'img_obj': img_object, 'result':q})  
    else:  
        form = UserImageForm()  
  
    return render(request, 'image_form.html', {'form': form})  