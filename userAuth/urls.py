from django.urls import path

from userAuth.auth_controller.auth_control import UserSignUp,UserLogin,TokenInfo,\
    ProfileCreation,UploadProfilePhoto

urlpatterns = [

    path('signup', UserSignUp.as_view()),
    path('signin', UserLogin.as_view()),
    path('user', TokenInfo.as_view()),
    path('photo/<int:id>',UploadProfilePhoto.as_view()),
    path('profile/<int:id>',ProfileCreation.as_view()),
    # path('profile/<int:id>',ProfileView.as_view()),
    # path('profile/<int:id>',ProfileDelete.as_View()),
]

