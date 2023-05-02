from django.urls import path
from . import views

urlpatterns = [
    
    path("",views.index,name="upload"),
    path("upload",views.index),
    path('upload/delete_image/<int:image_id>/',views.deleteImage,name='delete_image'),
    path('upload/download/<int:image_id>/',views.downloadImage,name='download_image'),
]