from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.contrib import messages
from .form import ImageForm
from .models import Image
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied


@login_required
def index(request):

    form = ImageForm(data=request.POST, files=request.FILES)
    if request.method == "POST":

        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            

            image = form.save(commit=False)
            image.user = request.user
            image.save()
            obj = form.instance
            return render(request, "prescription.html", {"obj": obj})


        else:
            form = ImageForm()
    img = Image.objects.filter(user=request.user)
    
    return render(request, "prescription.html",{"img": img, "form": form})

@login_required
def deleteImage(request,image_id):
    img = Image.objects.filter(id = image_id)
    img.delete()
    messages.success(request,"Image delted")
    return redirect('upload')

@login_required
def downloadImage(request, image_id):
    image = Image.objects.get(id=image_id)
    # Check if the current user is the owner of the image
    if request.user != image.user:
        raise PermissionDenied()
    response = HttpResponse(image.image, content_type=image.content_type)

    response['Content-Disposition'] = f'attachment; filename="{image.image.name}"'
    return response
