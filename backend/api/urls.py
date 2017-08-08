from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'ideas', views.IdeasViewSet)
router.register(r'players', views.PlayersViewSet)
router.register(r'game', views.GameViewSet)
router.register(r'winner', views.WinnerViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]