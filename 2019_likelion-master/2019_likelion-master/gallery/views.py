from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Photo
# Create your views here.

def show(request):
    photos = Photo.objects.all

    return render(request,'show_gallery.html',{
        'photos' : photos
    })

def read(request,photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    return render(request,'read_gallery.html',{
    'photo':photo
    })
