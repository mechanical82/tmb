from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from . import views
# from home import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.HomeIndex.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('nature/', views.nature, name='nature'),
    path('nature/post/<int:post_id>/', views.single_nature, name='post'),
    path('policy/', views.policy, name='policy'),
    path('search/', views.search, name='search'),
    path('culc/', views.culc, name='culc'),

    # path('diamonds/', cache_page(60)(views.diamonds), name='diamonds'),
    path('diamonds/', views.diamonds, name='diamonds'),
    path('clips/', views.clips, name='clips'),
    path('weddingrings/', views.weddingrings, name='weddingrings'),
    path('earrings/', views.earrings, name='earrings'),
    path('amulets/', views.amulets, name='amulets'),
    path('rings/', views.rings, name='rings'),
    path('request/', views.callback_request, name='callback-request'),
    path('callbacktelegram/', views.callbacktelegram_form, name='callbacktelegram_form'),

    path('price/', views.price, name='price'),    
    path('badges/', views.badges, name='badges'),    
    path('cast/', views.cast, name='cast'),    
    path('electroplating/', views.electroplating, name='electroplating'),    
    path('sketches/', views.sketches, name='sketches'),    
    path('models/', views.models, name='models'),    

    
    # add a flag for
# handling the 404 error
# handler404 = 'pages.views.error_404_view'
    # path('cats/<int:catid>/', categories),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]
