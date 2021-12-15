
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include(('users.urls','user'),namespace = 'users')),
    path('', include(('Learning_Logs.urls','Learning_Logs'),namespace='Learning_Logs')),
    
]
