from api.viewsets import CheckInViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Checkin', CheckInViewset)