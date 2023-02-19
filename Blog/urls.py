from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.publicaciones, name='publicaciones'),
    path('<int:publicacion_id>', views.publicacion_id, name='publicacion_id'),
]
