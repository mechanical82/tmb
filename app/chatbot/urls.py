from django.urls import path, re_path
# from .views import chatbot_view

from chatbot.views import *

urlpatterns = [
    # path('', home, name='home'),
    path('chabot', chatbot, name='chatbot'),
    # path('', chatbot_view, name='chat'),

    # path('about', about, name='about'),

    
    # add a flag for
# handling the 404 error
# handler404 = 'pages.views.error_404_view'
    # path('cats/<int:catid>/', categories),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]
