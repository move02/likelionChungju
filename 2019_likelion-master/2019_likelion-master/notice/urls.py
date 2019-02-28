from django.urls import path
from . import views

app_name ='notice'

urlpatterns = [
    path('show',views.show,name="show_list"),
    path('read/<int:post_id>',views.read,name="read_detail"),
    path('create',views.create,name="create"),
    path('edit/<int:post_id>',views.edit, name="edit"),
    path('destroy/<int:post_id>',views.destroy, name="destroy"),
    path('read/<int:post_id>/comment_create',views.comment_create, name="comment_create"),
    path('read/<int:comment_id>/comment_destroy',views.comment_destroy, name="comment_destroy"),   
]
