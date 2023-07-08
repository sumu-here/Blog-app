from django.urls import path
from accounts import views

app_name="accounts"

urlpatterns = [
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('register/',views.register,name='register'),

    ]