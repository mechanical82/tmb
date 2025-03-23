from django.contrib import admin
from django.urls import path, include
from home.views import *
from user.views import *
# from polls.views import *
from app import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('chatbot.urls')),
    path('', include('chat.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('', include('user.urls')),

    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/register/', views.register, name='register'),
    # path('accounts/password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/', include('allauth.urls')),
    
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('accounts/register/', views.register, name='register'),
#     path('accounts/password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
#     path('accounts/', include('django.contrib.auth.urls')),
# ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
