# env Modules
from rest_framework import routers
from rest_framework.routers import DefaultRouter

# My Modules
from api.user.views import *

router = routers.DefaultRouter()

# router = routers.SimpleRouter()

router.register(r'User', UserViewSet, basename='User')

urlpatterns = router.urls




