from django.urls import path
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib import admin
from pages import views

urlpatterns = [
        path('', views.login_render, name='Login'),
        path('home/', views.homepage_render, name="Homepage"),
        path('signup/', views.signup_render, name="Signup"),
        path('profile/', views.profile_render, name="Profile"),
        path('waivers/', views.waiver_render, name="Waivers"),
        path('inspections/', views.inspection_render, name="Inspections"),
        path('schedule/', views.schedule_render, name="Schedule"),
        path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
