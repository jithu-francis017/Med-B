from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

from .form import ImageForm
from .models import Image


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
