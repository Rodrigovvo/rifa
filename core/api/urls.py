from . import views
from django.urls import include
from django.urls import path
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'raffles', views.RaffleViewSet)
router.register(r'campaigns', views.CampaignViewSet)
router.register(r'tickets', views.TicketViewSet)
router.register(r'prizes', views.PrizeViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework'))
]
