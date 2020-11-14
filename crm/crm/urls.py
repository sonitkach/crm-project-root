from rest_framework import routers
from crmapp.views import CompanyListView, SpecialityListView, EmployeeListView

router = routers.DefaultRouter()
router.register(r'companies', CompanyListView)
router.register(r'specialities', SpecialityListView)
router.register(r'employees', EmployeeListView)

urlpatterns = router.urls