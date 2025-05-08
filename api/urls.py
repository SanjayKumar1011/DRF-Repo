from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
#Function Based Views

router= DefaultRouter()
router.register('employees',views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path('students/',views.studentsview),
    path('students/<int:pk>', views.studentDetailView),
    # for upto generics
    # path('employees',views.Employees.as_view()),
    # path('employees/<int:pk>', views.EmployeeDetail.as_view())

    # for view sets
    path('', include(router.urls))

]
