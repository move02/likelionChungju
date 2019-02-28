from django.urls import path
from . import views


app_name ='gallery'

urlpatterns = [
    path('show',views.show,name="show_gallery"),
    path('read/<int:photo_id>',views.read,name="read_gallery"),
]