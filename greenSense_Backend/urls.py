"""greenSense_Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from greenSense_Backend import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('user', views.UserViewSet)
router.register('chat', views.ChatViewSet)
router.register('message', views.MessageViewSet)
router.register('question', views.QuestionViewSet)

urlpatterns = [
    path('gs/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('accounts/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


