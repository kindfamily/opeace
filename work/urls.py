from django.urls import path
from .views import *

app_name = 'work'

urlpatterns = [
    # path('signup/', signup, name='signup'),
    path('/', login_check, name='login'),
    # path('logout/', logout, name='logout'),  
]