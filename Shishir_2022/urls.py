from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
from rest_framework import routers
import rest_framework
from apis import views

router = routers.DefaultRouter()

router.register('year', views.YearView, basename='year')
router.register('events', views.EventView, basename='events')
router.register('teammembers', views.TeamMemberView, basename='teammember')
router.register('gallery', views.GalleryView, basename='gallery')
router.register('notification', views.NotificationView,
                basename='notification')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'^froala_editor/', include('froala_editor.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)