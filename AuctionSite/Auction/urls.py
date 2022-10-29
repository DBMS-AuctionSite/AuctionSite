from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.registerPage, name="register"),
     
    path('logout/', views.logoutUser, name="logout"),
    path('profile/', views.profilePage, name="profile"),
    path('sell/', views.sellPage, name="sell")

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

