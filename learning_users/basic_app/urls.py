from django.urls import path
from . import views

# TEMPLATE URLS!
app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.registration, name='registration'),
    path('logout', views.user_logout, name='logout'),
    path('special', views.special, name='special'),
    path('user_login', views.user_login, name='user_login'),
]
