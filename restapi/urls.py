from django.urls import path
from restapi.controller.TestController import TestAPI
from restapi.controller.EmployeeController import EmployeeDetails
from restapi.controller.EmployeeController import EmployeeSearch
from restapi.controller.registration_controller import RegistrationDetails,ValidEmail,RegisterList

#test git changes

urlpatterns = [

    path('test-api',TestAPI.as_view()),
    path('employee',EmployeeDetails.as_view()),
    path('employee/<int:id>',EmployeeSearch.as_view()),
    path('register',RegistrationDetails.as_view()),
    path('validateEmail/<str:email>',ValidEmail.as_view()),
    path('register/<int:id>', RegisterList.as_view())
]