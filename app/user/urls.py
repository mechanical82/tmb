from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from user.views import *
from . import views

urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),

    
    # add a flag for
# handling the 404 error
# handler404 = 'pages.views.error_404_view'
    # path('cats/<int:catid>/', categories),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]
