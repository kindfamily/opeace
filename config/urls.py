from django.contrib import admin
from django.urls import include, path
from work.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', home, name='root'),
    path('start/', start, name='start'),
    path('working/', working, name='working')
]