from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    # path('signup/', signup, name='signup'),
    path('login/', login_check, name='login_check'),
    path('logout/', logout, name='logout'),  
]