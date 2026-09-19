from django.shortcuts import render ,redirect
from .models import upload_files
from .forms import upload_file_form
from django.contrib import messages
# Create your views here.
def display_files(request):
    files = upload_files.objects.all()
    return render(request,'img_display.html',{'files':files})

def upload_file(request):
    if request.method =='POST':
        form = upload_file_form(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Image uploaded successfully! 🎉")
            
            return redirect('display_files')
    else:
        form = upload_file_form()
    return render(request,'img_upload.html',{'form':form})