from django.urls import path
from . import views
from.views import home
from.views import culture
from.views import signup
from.views import loginpage
from.views import signout
from.views import destinations

urlpatterns = [
    path("", home, name='Homepage'),
    path('Culture/', culture, name='culture'),
     path('Signup/', signup, name='signup'),
    path('loginpage/',   loginpage, name='loginpage'),
    path ('logout/' , signout, name='logout'),
    path('Destinations/',   destinations, name='destinations')

    
    ]
