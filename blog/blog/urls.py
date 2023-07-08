from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('addpost/', views.addpost, name='addpost'),
    path('detail/<slug:slug>/', views.detail, name='detail'),
    path('update/<slug:slug>/', views.update, name='update'),
    path('delete/<str:model>/<int:pk>/', views.delete_item, name='delete_item'),
    
    ]
