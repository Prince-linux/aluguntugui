from django.urls import path
from .views import *

app_name = 'profiles'
urlpatterns = [
    path('<int:uid>/view', view_profile, name='view'),
]
