from django.urls import path

from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('choose_gallery', views.choose_gallery, name='choose_gallery'),
    path('<int:pk>/', views.collection_index, name='collection_index'),
    path('<int:collection_id>/<int:art_id>/', views.art_details, name='art_details'),
]