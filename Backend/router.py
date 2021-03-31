from qr_scan.viewsets import CheckInViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('checkin', CheckInViewset)

#for url in router.urls:
#    print(url, '\n')