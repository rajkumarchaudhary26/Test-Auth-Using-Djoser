from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users import api
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('profile', api.ProfileViewSet, basename='profile')
router.register('user', api.UserViewSet, basename = 'user')
router.register('award', api.AwardViewSet, basename='award')
router.register('language', api.LanguageViewSet, basename = 'language')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-auth/', include("rest_framework.urls")),
    path('', include(router.urls)),
]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)