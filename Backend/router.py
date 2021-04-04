from qr_scan.viewsets import CheckInViewset
#from status.viewsets import DateViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('checkin', CheckInViewset)
#router.register('date', DateViewset)

#for url in router.urls:
#    print(url, '\n')