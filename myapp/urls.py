from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home/',views.home,name='home'), 
    path('download_file/<int:id>',views.download_file,name='download_file'),
    path('delete_file/<int:id>',views.delete_file,name='delete_file'),
    path('file_summary/<int:id>/', views.file_summary, name='file_summary'),
]
